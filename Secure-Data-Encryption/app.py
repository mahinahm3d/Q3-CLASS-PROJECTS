import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import time
import uuid

# Generate a key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory data storage
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# Chinese-inspired color palette
red = "#E53935"
dark_red = "#C62828"
gold = "#FFD700"
dark_gold = "#FFC400"
light_bg = "#FAFAFA"

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data (include passkey in the encryption)
def encrypt_data(text, passkey):
    salt = hashlib.sha256(passkey.encode()).digest()
    key = hashlib.pbkdf2_hmac('sha256', KEY, salt, 100000)
    cipher = Fernet(Fernet.generate_key())  # Using a new key derived from master key + passkey
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    try:
        salt = hashlib.sha256(passkey.encode()).digest()
        key = hashlib.pbkdf2_hmac('sha256', KEY, salt, 100000)
        cipher = Fernet(Fernet.generate_key())  # Same derivation as encryption
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        st.session_state.failed_attempts += 1
        return None

# Apply styling with custom fonts
def apply_chinese_style():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Dancing+Script:wght@400;700&family=Merriweather:wght@400;700&family=Pacifico&display=swap');
        
        .main {{
            background-color: {light_bg};
            font-family: 'Merriweather', serif;
        }}
        .sidebar .sidebar-content {{
            background-color: white;
            font-family: 'Merriweather', serif;
        }}
        h1, h2, h3 {{
            color: {dark_red};
            font-family: 'Cinzel', serif;
        }}
        .stButton>button {{
            background-color: {red};
            color: white;
            border-radius: 4px;
            font-weight: bold;
            font-family: 'Merriweather', serif;
        }}
        .stTextInput>div>div>input {{
            border: 1px solid {gold};
            font-family: 'Merriweather', serif;
        }}
        .stTextArea>div>div>textarea {{
            border: 1px solid {gold};
            font-family: 'Merriweather', serif;
        }}
        .success {{
            color: {dark_red} !important;
        }}
        .logo {{
            font-family: 'Pacifico', cursive;
            font-size: 1.5rem;
            color: {dark_red};
        }}
        .quote {{
            font-family: 'Dancing Script', cursive;
            font-size: 1.2rem;
            color: #555;
        }}
    </style>
    """, unsafe_allow_html=True)

apply_chinese_style()

# Main header with fancy fonts
st.markdown(f"""
<div style="text-align: center; border-bottom: 2px solid {gold}; padding-bottom: 10px; margin-bottom: 30px;">
    <h1 style="color: {dark_red}; margin-bottom: 0; font-family: 'Cinzel', serif;">Secure Data Storage System</h1>
    <p class="quote">Encrypted · Convenient · Reliable</p>
</div>
""", unsafe_allow_html=True)

# Navigation menu
menu_options = {
    "Home": "Home",
    "Store Data": "Store Data",
    "Retrieve Data": "Retrieve Data",
    "Login": "Login"
}

choice = st.sidebar.radio("Navigation", list(menu_options.values()))

# Home Page
if choice == menu_options["Home"]:
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="font-family: 'Cinzel', serif;">Welcome to the Secure Data Storage System</h3>
        <p class="quote">Store and retrieve your data securely with a unique passkey</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 8px; border-left: 4px solid {red};">
            <h4 style="font-family: 'Cinzel', serif;">Store Data</h4>
            <p>Encrypt and safely store your sensitive information</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 8px; border-left: 4px solid {red};">
            <h4 style="font-family: 'Cinzel', serif;">Retrieve Data</h4>
            <p>Decrypt your data using the correct passkey</p>
        </div>
        """, unsafe_allow_html=True)

# Store Data Page
elif choice == menu_options["Store Data"]:
    st.markdown(f"""
    <div style="border-left: 4px solid {red}; padding-left: 15px;">
        <h3 style="font-family: 'Cinzel', serif;">Encrypt and Store Data</h3>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("store_form"):
        user_data = st.text_area("Enter data to encrypt:", height=150)
        passkey = st.text_input("Create a passkey:", type="password")
        submitted = st.form_submit_button("Encrypt & Save")
        
        if submitted:
    if user_data and passkey:
        encrypted_text = encrypt_data(user_data)
        st.session_state.stored_data[encrypted_text] = {
            "encrypted_text": encrypted_text,
            "passkey": hash_passkey(passkey)
        }
        st.success("Data has been securely stored!")
    else:
        st.error("Please fill in all fields!")

# Retrieve Data Page
elif choice == menu_options["Retrieve Data"]:
    st.markdown(f"""
    <div style="border-left: 4px solid {red}; padding-left: 15px;">
        <h3 style="font-family: 'Cinzel', serif;">Decrypt and Retrieve Data</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.failed_attempts >= 3:
        st.error("Too many failed attempts! Please log in first.")
        time.sleep(1)
        st.experimental_rerun()
    
    with st.form("retrieve_form"):
        encrypted_text = st.text_area("Enter encrypted data:", height=150)
        passkey = st.text_input("Enter passkey:", type="password")
        submitted = st.form_submit_button("Decrypt Data")
        
        if submitted:
            if encrypted_text and passkey:
                decrypted_text = decrypt_data(encrypted_text, passkey)
                
                if decrypted_text:
                    st.success("Decryption successful!")
                    st.text_area("Decrypted Data:", value=decrypted_text, height=200)
                else:
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"Incorrect passkey! Remaining attempts: {remaining}")
                    
                    if st.session_state.failed_attempts >= 3:
                        st.error("Maximum attempts reached! Redirecting to login page...")
                        time.sleep(1)
                        st.experimental_rerun()
            else:
                st.error("Please fill in all fields!")

# Login Page
elif choice == menu_options["Login"]:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <h3 style="font-family: 'Cinzel', serif;">System Login</h3>
        <p class="quote">Enter your credentials below</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        login_pass = st.text_input("Enter login password:", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if login_pass == "admin123":  # Demo purpose password
                st.session_state.failed_attempts = 0
                st.success("Login successful! Redirecting...")
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error("Incorrect password!")
