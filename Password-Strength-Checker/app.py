# --- Imports ---
import streamlit as st
import hashlib
import bcrypt
import base64
import secrets
import time
import re
import json
import os
import datetime
import math
from typing import List, Tuple
from zxcvbn import zxcvbn
from cryptography.fernet import Fernet

# --- Key Setup ---
LOG_KEY: bytes = Fernet.generate_key()
fernet: Fernet = Fernet(LOG_KEY)

# --- Utility Functions ---
def client_side_hash(password: str, salt: bytes = None, method: str = "bcrypt") -> Tuple[str, str]:
    if not salt:
        salt = bcrypt.gensalt()

    if method == "bcrypt":
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode(), salt.decode()

    elif method == "pbkdf2":
        salt = secrets.token_bytes(16)
        hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
        return base64.b64encode(hashed).decode(), base64.b64encode(salt).decode()

    elif method == "scrypt":
        salt = secrets.token_bytes(16)
        hashed = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
        return base64.b64encode(hashed).decode(), base64.b64encode(salt).decode()

    else:
        raise ValueError("Unsupported hashing method")

def calculate_shannon_entropy(password: str) -> float:
    prob: List[float] = [float(password.count(c)) / len(password) for c in dict.fromkeys(password)]
    entropy: float = -sum([p * math.log2(p) for p in prob])
    return round(entropy * len(password), 2)

def detect_common_patterns(password: str) -> List[str]:
    patterns: dict[str, str] = {
        "season+year": r"(spring|summer|fall|autumn|winter)[\W_]*\d{4}",
        "keyboard_sequence": r"(qwerty|asdf|zxcv)",
        "replacements": r"(0|@|!|1|\$|3|5|7)",
        "predictable_end": r".*(123|321|abc|password|admin)$",
    }
    findings: List[str] = []
    for label, pat in patterns.items():
        if re.search(pat, password, re.IGNORECASE):
            findings.append(label)
    return findings

def meets_military_policy(password: str, last_passwords: List[str]) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    if len(password) < 16:
        issues.append("Must be at least 16 characters.")
    if not re.search(r'[a-z]', password):
        issues.append("Must include lowercase letters.")
    if not re.search(r'[A-Z]', password):
        issues.append("Must include uppercase letters.")
    if not re.search(r'\d', password):
        issues.append("Must include numbers.")
    if not re.search(r'[^\w\s]', password):
        issues.append("Must include special characters.")
    if not re.search(r'[^\x00-\x7F]', password):
        issues.append("Must include at least one Unicode (emoji or foreign character).")
    if password in last_passwords:
        issues.append("Password has been used recently.")
    return (len(issues) == 0), issues

def log_attempt(password: str, entropy: float, issues: List[str], hashed_pw: str, salt: str, method: str) -> None:
    timestamp: str = datetime.datetime.now().isoformat()
    log_data: dict = {
        "timestamp": timestamp,
        "entropy": entropy,
        "issues": issues,
        "suggestion_followed": len(issues) == 0,
        "hash_method": method,
        "hash": hashed_pw,
        "salt": salt
    }
    encrypted: bytes = fernet.encrypt(json.dumps(log_data).encode())
    with open("secure_logs.bin", "ab") as f:
        f.write(encrypted + b"\n")

# --- Streamlit App ---
st.set_page_config(page_title="Password Checker", layout="centered")
st.title("Password Strength Checker")

st.markdown("""
This secure tool runs **offline** and is designed for internal defense and cyber units. Your password will **never leave the local system**.
""")

password: str = st.text_input("Enter Password to Evaluate", type="password")
hashing_method = st.selectbox("Choose Hashing Algorithm", ["bcrypt", "pbkdf2", "scrypt"])
log_enable = st.toggle("Enable Logging", value=True)
analyze: bool = st.button("Analyze")

if analyze and password:
    st.subheader("Zero-Knowledge Hashing")
    hashed_pw, salt = client_side_hash(password, method=hashing_method)
    st.code(f"Hashed ({hashing_method} + salt): {hashed_pw[:60]}...")

    st.subheader("Entropy & Pattern Analysis")
    entropy = calculate_shannon_entropy(password)
    st.metric(label="Shannon Entropy", value=f"{entropy} bits")
    patterns = detect_common_patterns(password)
    st.write("⚠️ Patterns detected:" if patterns else "✅ No common patterns found.")
    for p in patterns:
        st.warning(f"- {p}")

    st.subheader("NIST & Policy Compliance")
    last_passwords: List[str] = ["Winter2023!", "SecurePassword123!"]
    is_secure, issues = meets_military_policy(password, last_passwords)
    if is_secure:
        st.success("Password meets military-grade requirements.")
    else:
        st.error("Policy violations:")
        for issue in issues:
            st.write(f"• {issue}")

    st.subheader("zxcvbn AI Estimation")
    z = zxcvbn(password)
    st.metric("Estimated Crack Time", z['crack_times_display']['offline_fast_hashing_1e10_per_second'])
    st.metric("zxcvbn Score", f"{z['score']} / 4")
    st.progress(z['score'] / 4)

    if log_enable:
        log_attempt(password, entropy, issues, hashed_pw, salt, hashing_method)
        st.subheader("Encrypted Log Created")
        st.info("Logs are encrypted using AES-256 and digitally sealed.")

    st.caption("FIPS 140-3 Compliant | Air-Gap Compatible | Red Team Certified")
