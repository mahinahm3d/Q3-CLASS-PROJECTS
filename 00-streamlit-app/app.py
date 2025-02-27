import streamlit as st
import dis
import pandas as pd

# Title
st.title("Python Fundamentals and Execution")
st.write("This Streamlit app summarizes key concepts from the first class on Python.")

# Section 1: Python Introduction
st.header("1️⃣ Introduction to Python")
st.write(
    "Python was created by **Guido van Rossum** in the late 1980s and officially released in 1991. "
    "It is dynamically typed, meaning you don't need to specify variable types like `int`, `float`, or `str` explicitly."
)

# Section 2: Print Function
st.header("2️⃣ Python Print Function")
st.write("Unlike `Print`, `print` (lowercase) is the correct built-in function to display output.")
st.code("print('Hello, World!')", language="python")

# Section 3: Python Execution Process
st.header("3️⃣ Python Execution Process")
st.write("When you run a Python script, it follows this process:")
st.markdown("""
1. **Source Code (.py file)** → Written by the user.
2. **Bytecode (.pyc file or in-memory)** → Python compiles the .py file into bytecode.
3. **Python Virtual Machine (PVM)** → Executes the bytecode line by line.
""")

# Section 4: Bytecode Analysis
st.header("4️⃣ Bytecode Analysis")
st.write("Python code is first compiled into bytecode before execution. Let's analyze a simple function:")

def sample_function():
    print("Hello, Bytecode!")

bytecode = dis.Bytecode(sample_function)
st.code("\n".join([str(instr) for instr in bytecode]), language="python")

# Section 5: Python Use Cases
st.header("5️⃣ Python Use Cases")
st.write("Python is used in various domains. Here's a table summarizing its applications:")

data = {
    "Category": ["Web Development", "Data Science & ML", "Automation", "Cybersecurity", "Game Development"],
    "Example Libraries": ["Django, Flask", "Pandas, TensorFlow", "Selenium, PyAutoGUI", "Scapy, Paramiko", "Pygame, Panda3D"],
    "Use Cases": [
        "Websites, Web Apps",
        "AI, Data Analytics",
        "Auto-Email, File Management",
        "Ethical Hacking, Pen Testing",
        "2D/3D Games"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)

# Section 6: GPU vs TPU Comparison
st.header("6️⃣ GPU vs TPU Comparison")
st.write("Comparison of GPUs and TPUs in different applications:")

data_gpu_tpu = {
    "Task": ["Gaming", "Video Editing", "AI Model Training (PyTorch)", "AI Model Training (TensorFlow)", "AI Inference (Production)"],
    "Use GPU?": ["✅ Yes", "✅ Yes", "✅ Yes", "✅ Yes", "✅ Yes"],
    "Use TPU?": ["❌ No", "❌ No", "❌ No", "✅ Yes (Faster)", "✅ Yes (Faster)"]
}

df_gpu_tpu = pd.DataFrame(data_gpu_tpu)
st.dataframe(df_gpu_tpu)

# Section 7: Python Built-in Data Types
st.header("📌 Python Built-in Data Types")

data_types = {
    "Data Type": ["String (str)", "Integer (int)", "Float (float)", "Boolean (bool)",
                  "List (list)", "Tuple (tuple)", "Dictionary (dict)", "Set (set)",
                  "Frozen Set (frozenset)", "NoneType"],
    "Description": ["Text data", "Whole numbers", "Decimal values", "True / False",
                    "Ordered, mutable collection", "Ordered, immutable collection",
                    "Key-value pairs", "Unordered, unique collection",
                    "Immutable version of set", "Represents 'nothing'"],
    "Example": ['"Hello"', "10", "3.14", "False",
                '["a", "b", "c"]', '("x", "y")', '{"name": "Ali"}',
                "{1, 2, 3}", "frozenset([1, 2, 3])", "None"]
}

df_data_types = pd.DataFrame(data_types)
st.dataframe(df_data_types)

# Section 8: PEP 8 - Python Style Guide
st.header("📌 PEP 8 – Python Style Guide")

st.subheader("1️⃣ Indentation (Use 4 Spaces)")
st.code('''def hello():
    print("Hello, World!")  # 4 spaces''', language="python")

st.subheader("2️⃣ Maximum Line Length (79 Characters)")
st.code('''text = ("This is a long string that is split "
        "into multiple lines for readability.")''', language="python")

st.subheader("3️⃣ Blank Lines")
st.code('''class MyClass:
    
    def method_one(self):
        pass
    
    def method_two(self):
        pass''', language="python")

st.subheader("4️⃣ Naming Conventions")
st.code('''student_name = "Ali"  # Correct (snake_case)
class StudentDetails:  # Correct (PascalCase)
    pass
MAX_LIMIT = 100  # Constants in ALL_CAPS''', language="python")

st.subheader("5️⃣ Imports (One per Line)")
st.code('''import os
import sys''', language="python")

st.subheader("6️⃣ Whitespace Rules")
st.code('''x = (1, 2, 3)  # Correct
result = x + y  # Correct''', language="python")

st.subheader("7️⃣ Comments (Use # for Single Line, ''' ''' for Docstrings)")
st.code('''# This is a comment
def add(a, b):
    """This function adds two numbers."""
    return a + b''', language="python")

st.subheader("8️⃣ Use 'is' for None Comparison")
st.code('''if value is None:
    pass''', language="python")

st.subheader("9️⃣ Avoid Using 'from module import *'")
st.code('''from math import sqrt, pi  # Correct''', language="python")

st.subheader("🔟 Example of PEP 8 Compliant Code")
st.code('''import os
import sys

MAX_LIMIT = 100

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

class Calculator:
    
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

calc = Calculator()
calc.add(5)
print(calc.value)''', language="python")

st.write("This concludes the Python summary. Happy coding! 🚀")
