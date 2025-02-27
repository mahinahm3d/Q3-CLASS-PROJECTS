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

st.write("This concludes the Python summary. Happy coding! 🚀")
