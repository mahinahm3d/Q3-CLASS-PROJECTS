import streamlit as st
import dis
import pandas as pd

# Title
st.title("Python Fundamentals and Execution")
st.write("This Streamlit app summarizes key concepts from the first class on Python.")

# Section 1: Introduction to Python
st.header("1️⃣ Introduction to Python 🐍")
st.write(
    "Python was created by **Guido van Rossum**, a Dutch programmer, in the late 1980s. "
     "He officially released **Python 0.9.0 in 1991**, featuring simple syntax similar to English. "
    "Python is dynamically typed, so you don't need to declare types explicitly, but you can use type hints 🎯"
)

st.markdown("### Printing Output in Python 🖨️")
st.write(
    "In Python, the **`print()`** function is used to display output on the screen. "
    "It is a built-in function and one of the first commands beginners learn. "
    "Remember, using `Print` (uppercase) will cause a **NameError**, while `print` (lowercase) works correctly. ✅"
)

st.markdown("### Example:")
st.code("print('Hello, World!')", language="python")


# Section 2: Python Execution Process & Bytecode Analysis 🔄🔍
st.header("2️⃣ Python Execution Process & Bytecode Analysis 🔄🔍")
st.write("When you run a Python script, it goes through the following steps:")
st.markdown(
    """
1️⃣ **Source Code (`.py` file)** – Human-readable Python code.  
2️⃣ **Bytecode (`.pyc` file or in-memory bytecode)** – Python compiles the code into bytecode.  
3️⃣ **Python Virtual Machine (PVM)** – Executes bytecode line by line.  
"""
)
st.markdown("💡 Python abstracts machine-level execution, unlike compiled languages like C++.")

st.write(
    "**What happens under the hood?** Python first compiles your code into bytecode before execution. "
    "This bytecode is stored in `.pyc` files (inside `__pycache__`) or kept in memory."
)

st.markdown("### Example Bytecode Analysis:")
st.code(
    """
import dis

def greet():
    print("Hello, World!")

dis.dis(greet)
""",
    language="python",
)

st.markdown("### Output (Bytecode Instructions):")
st.code(
    """
  2           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello, World!')
              4 CALL_FUNCTION            1
              6 RETURN_VALUE
""",
    language="text",
)

st.write(
    "This is Python’s low-level **bytecode**, interpreted by the **Python Virtual Machine (PVM).** 🖥️ "
    "Understanding bytecode helps in performance tuning, debugging, and security. 🔍"
)

# Section 3: Python’s Dynamic Typing & PVM 🖥️
st.header("3️⃣ Python’s Dynamic Typing & PVM 🖥️")
st.write(
    "**Python is dynamically typed, meaning you don't need to specify variable types explicitly.** "
    "The interpreter determines types at runtime."
)
st.markdown("### Example:")
st.code(
    """
x = 5      # Integer
x = "Hello"  # String (Python allows changing types)
""",
    language="python",
)
st.markdown("💡 Unlike statically typed languages like C++, Python allows type flexibility.")

st.write(
    "Python's **PVM** executes bytecode instructions **one by one**, converting them into machine code dynamically."
)
st.markdown("### Why is this important?")
st.markdown(
    """
✅ **Makes Python cross-platform** – Bytecode is platform-independent.  
✅ **Handles memory management** – Uses garbage collection for optimization.  
✅ **Supports interactive execution** – Great for prototyping and scripting.  
"""
)

# Section 4: Reverse Engineering `.pyc` Files 🔍
st.header("4️⃣ Reverse Engineering `.pyc` Files 🔍")
st.write(
    "Python `.pyc` files contain compiled bytecode. **Can they be decompiled?** 🧐"
)
st.markdown("✅ Yes, but with some limitations:")
st.markdown(
    """
- **Obfuscation** – Some developers use tools like PyArmor to protect code.  
- **Cython or PyInstaller** – These make decompilation harder.  
- **Stripped Debug Symbols** – Removes variable names, making reverse engineering difficult.  
"""
)
st.markdown("### Example: Decompiling `.pyc` with `uncompyle6` (⚠️ Ethical Use Only!)")
st.code("uncompyle6 -o output_dir my_script.pyc", language="bash")

st.markdown("🔴 **Warning:** Reverse engineering should only be done for ethical and legal purposes!")

# Section 6: GPU vs TPU Comparison
# Explanation of GPU
st.subheader("🖥️ What is a GPU?")
st.write("""
A **GPU (Graphics Processing Unit)** is a powerful chip designed for **parallel computing**. Originally made for gaming, it's now widely used in:
- AI & Deep Learning
- 3D Rendering & Video Editing
- Scientific Simulations
""")

st.markdown("**Popular GPUs:**")
st.code('''NVIDIA: RTX 3090, A100, H100
AMD: Radeon RX 7900 XTX
Apple: M1/M2 GPU''', language="plaintext")

# Explanation of TPU
st.subheader("⚡ What is a TPU?")
st.write("""
A **TPU (Tensor Processing Unit)** is a specialized AI chip created by **Google**. It’s optimized for **TensorFlow** and performs matrix operations **faster and more efficiently** than a GPU.
""")

st.markdown("**Where Are TPUs Used?**")
st.markdown("""
- **Google Cloud AI**
- **AI-powered search results**
- **Google Translate, Photos, and Assistant**
- **TensorFlow models**
""")

# GPU vs TPU Comparison
st.header("🔍 GPU vs TPU Comparison")
st.write("Comparison of GPUs and TPUs in different applications:")

# Data for GPU vs TPU comparison
data_gpu_tpu = {
    "Task": [
        "Gaming", 
        "Video Editing & 3D Design", 
        "AI Model Training (PyTorch)", 
        "AI Model Training (TensorFlow)", 
        "AI Inference (Production)", 
        "Cloud AI Computing"
    ],
    "Use GPU?": [
        "✅ Yes", 
        "✅ Yes", 
        "✅ Yes", 
        "✅ Yes", 
        "✅ Yes", 
        "❌ No"
    ],
    "Use TPU?": [
        "❌ No", 
        "❌ No", 
        "❌ No", 
        "✅ Yes (Faster)", 
        "✅ Yes (Faster)", 
        "✅ Yes (Google Cloud TPUs)"
    ]
}

# Create and display DataFrame
df_gpu_tpu = pd.DataFrame(data_gpu_tpu)
st.dataframe(df_gpu_tpu)

# When to Use GPU or TPU
st.subheader("🤔 Which One Should You Use?")

st.success("✅ **Choose a GPU if:**")
st.markdown("""
- You're using **PyTorch, OpenAI models, or gaming**.
- You need **CUDA acceleration** for machine learning/deep learning.
""")

st.info("✅ **Choose a TPU if:**")
st.markdown("""
- You're using **TensorFlow models on Google Cloud**.
- You need **fast AI inference at low power cost**.
""")


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

# Section 9: Multiple Strings in Python (Different Ways to Work with Them)
st.header("📌 Multiple Strings in Python (Different Ways to Work with Them)")

st.subheader("1️⃣ Concatenation (+) → Joining Strings")
st.code('''str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World''', language="python")

st.warning("🚫 Wrong: Forgetting spaces can lead to incorrect output.")
st.code('''print("Hello" + "World")  # Output: HelloWorld (No space)''', language="python")

st.subheader("2️⃣ Using join() → Efficient for Multiple Strings")
st.code('''words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome''', language="python")

st.subheader("3️⃣ Using Triple Quotes (''' ''' or \"\"\" \"\"\") → Multi-line Strings")
st.code('''text = """This is a
multi-line
string in Python."""
print(text)''', language="python")

st.success("💡 Good for long texts & docstrings in functions or classes.")

st.subheader("4️⃣ Using Escape Sequences (\\n, \\t)")
st.code('''text = "Hello\\nWorld!"  # New line
print(text)''', language="python")

st.text("🔹 Other escape sequences:")
st.table({
    "Escape": ["\\n", "\\t", "\\\\", "\\'", "\\\""],
    "Meaning": ["New line", "Tab", "Backslash", "Single quote", "Double quote"]
})

st.subheader("5️⃣ Using f-strings (f\"\") → Formatting Multiple Strings")
st.code('''name = "Ali"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)''', language="python")

st.text("⏳ Older methods:")
st.code('''# Using format()
message = "My name is {} and I am {} years old.".format(name, age)

# Using % formatting (Old way)
message = "My name is %s and I am %d years old." % (name, age)''', language="python")

st.subheader("6️⃣ Using + with Numbers & Strings (str())")
st.warning("🚫 Wrong:")
st.code('''age = 25
message = "I am " + age + " years old."  # TypeError''', language="python")

st.success("✅ Correct:")
st.code('''message = "I am " + str(age) + " years old."''', language="python")

st.success("✅ Better (f-string):")
st.code('''message = f"I am {age} years old."''', language="python")

st.subheader("7️⃣ Repeating Strings (*)")
st.code('''print("Hello " * 3)  
# Output: Hello Hello Hello''', language="python")

st.subheader("8️⃣ Checking if a String Contains Another (in)")
st.code('''text = "Python is fun"
print("Python" in text)  # Output: True''', language="python")

st.subheader("9️⃣ Splitting and Combining Multiple Strings (split(), join())")
st.code('''text = "Python is fun"
words = text.split()  # Splits into ['Python', 'is', 'fun']
sentence = "-".join(words)  # Joins back: "Python-is-fun"''', language="python")

st.subheader("🚀 Summary Table")
st.table({
    "Method": ["Concatenation (+)", "join()", "Triple Quotes", "Escape Sequences", "f-strings", "Convert Numbers (str())", "Repeating Strings (*)", "Check Substring (in)", "Splitting (split())"],
    "Example": ['"Hello " + "World"', '" ".join(["Python", "is", "fun"])', '"""Multi-line string"""', '"Hello\\nWorld!"', 'f"My age is {age}"', '"Age: " + str(25)', '"Hello " * 3', '"Python" in text', '"Hello World".split()'],
    "Use Case": ["Simple joining", "Efficient multiple joins", "Multi-line text", "Formatting text", "String formatting", "Mixing numbers & strings", "Duplicate text", "Check if exists", "Break text into words"]
})

# Section 10: Multiple Integers in Python (Operations & Use Cases)
st.header("📌 Multiple Integers in Python (Operations & Use Cases)")

st.subheader("1️⃣ Basic Integer Operations")
st.code('''a = 10
b = 5

print(a + b)  # Addition → 15
print(a - b)  # Subtraction → 5
print(a * b)  # Multiplication → 50
print(a / b)  # Division (returns float) → 2.0
print(a // b) # Floor Division → 2 (removes decimals)
print(a % b)  # Modulus (remainder) → 0
print(a ** b) # Exponentiation → 10^5 = 100000''', language="python")

st.subheader("2️⃣ Using Multiple Integers in Variables")
st.code('''x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3''', language="python")

st.subheader("3️⃣ Converting Integers (int())")
st.code('''num = "123"
converted = int(num)  # Convert string to integer
print(converted + 1)  # Output: 124''', language="python")

st.warning("🚫 Wrong: Mixing types without conversion")
st.code('''age = "25"
print("My age is " + age)  # TypeError''', language="python")

st.success("✅ Correct:")
st.code('''print("My age is " + str(age))  # Output: My age is 25''', language="python")

st.subheader("4️⃣ Handling Large Integers (Arbitrary Precision)")
st.code('''big_number = 99999999999999999999999999
print(big_number * 2)''', language="python")

st.subheader("5️⃣ Integer Division (//) vs. Normal Division (/)")
st.code('''print(10 / 3)   # Output: 3.3333333333333335 (float)
print(10 // 3)  # Output: 3 (integer, removes decimal)''', language="python")

st.subheader("6️⃣ Checking Even or Odd (%)")
st.code('''num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")''', language="python")

st.subheader("7️⃣ Multiple Integers in a List (list)")
st.code('''numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1

# Sum of all integers
print(sum(numbers))  # Output: 15''', language="python")

st.subheader("8️⃣ Using Integers in Loops")
st.code('''for i in range(1, 6):
    print(i)  
# Output: 1 2 3 4 5''', language="python")

st.subheader("9️⃣ Finding Min, Max, Sum of Multiple Integers")
st.code('''nums = [10, 5, 30, 20]
print(max(nums))  # Output: 30 (largest number)
print(min(nums))  # Output: 5  (smallest number)
print(sum(nums))  # Output: 65 (sum of numbers)''', language="python")

st.subheader("🔟 Using Integers in f-strings (f\"\")")
st.code('''age = 25
print(f"My age is {age}")  # Output: My age is 25''', language="python")

st.subheader("🚀 Summary Table")
st.table({
    "Concept": ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)", "Floor Division (//)", "Modulus (%)", "Exponentiation (**)", "Convert String to Int (int())", "Even or Odd Check (%)", "Sum of List (sum())", "Finding Max (max())"],
    "Example": ["10 + 5", "10 - 5", "10 * 5", "10 / 5", "10 // 3", "10 % 3", "2 ** 3", "int('123')", "if x % 2 == 0:", "sum([1,2,3])", "max([1,2,3])"],
    "Output": ["15", "5", "50", "2.0 (float)", "3", "1 (remainder)", "8", "123", "Checks even/odd", "6", "3"]
})

# Section 11: Multiple Lists in Python (Operations & Use Cases)
st.header("📌 Multiple Lists in Python (Operations & Use Cases)")

st.subheader("1️⃣ Creating Multiple Lists")
st.code('''# Creating separate lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14, True]  # Different data types allowed

print(fruits)   # Output: ['apple', 'banana', 'cherry']
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed)    # Output: [10, 'hello', 3.14, True]''', language="python")

st.subheader("2️⃣ Accessing Elements in Lists (Indexing & Slicing)")
st.code('''fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[0])   # Output: apple  (first item)
print(fruits[-1])  # Output: orange (last item)
print(fruits[1:3]) # Output: ['banana', 'cherry'] (slicing)''', language="python")

st.subheader("3️⃣ Updating & Modifying Lists")
st.code('''fruits[1] = "mango"  
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']''', language="python")

st.subheader("4️⃣ Adding Multiple Lists Together (+)")
st.code('''list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]''', language="python")

st.subheader("5️⃣ Nesting Multiple Lists (List of Lists)")
st.code('''nested_list = [[1, 2, 3], ["apple", "banana"], [True, False]]
print(nested_list[0])   # Output: [1, 2, 3]
print(nested_list[1][0])  # Output: apple (first item of second list)''', language="python")

st.subheader("6️⃣ Appending and Extending Lists (append(), extend())")
st.code('''numbers = [1, 2, 3]
numbers.append(4)  # Adds a single item
print(numbers)  # Output: [1, 2, 3, 4]

numbers.extend([5, 6])  # Adds multiple items
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]''', language="python")

st.warning("🚫 Difference Between append() & extend()")
st.code('''list1 = [1, 2, 3]
list1.append([4, 5])  # Adds list as a single element
print(list1)  # Output: [1, 2, 3, [4, 5]]''', language="python")

st.success("✅ Use extend() instead for merging:")
st.code('''list1.extend([4, 5])
print(list1)  # Output: [1, 2, 3, 4, 5]''', language="python")

st.subheader("7️⃣ Removing Elements (remove(), pop(), del)")
st.code('''fruits = ["apple", "banana", "cherry", "orange"]

fruits.remove("banana")  # Removes specific element
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.pop(1)  # Removes by index
print(fruits)  # Output: ['apple', 'orange']

del fruits[0]  # Deletes first element
print(fruits)  # Output: ['orange']''', language="python")

st.subheader("8️⃣ Sorting & Reversing Lists (sort(), reverse())")
st.code('''numbers = [5, 2, 9, 1, 7]

numbers.sort()  # Sorts in ascending order
print(numbers)  # Output: [1, 2, 5, 7, 9]

numbers.reverse()  # Reverses order
print(numbers)  # Output: [9, 7, 5, 2, 1]''', language="python")

st.subheader("🔹 Sorting in Descending Order")
st.code('''numbers.sort(reverse=True)
print(numbers)  # Output: [9, 7, 5, 2, 1]''', language="python")

st.subheader("9️⃣ Iterating Through Multiple Lists (zip(), for loops)")
st.code('''names = ["Ali", "Ahmed", "Sara"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Output:
# Ali is 25 years old.
# Ahmed is 30 years old.
# Sara is 22 years old.''', language="python")

st.subheader("🔟 Copying Lists (copy(), list(), [:])")
st.code('''original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print(copy1, copy2, copy3)  # Output: [1, 2, 3] [1, 2, 3] [1, 2, 3]''', language="python")

st.warning("🚫 Wrong Way to Copy (Creates Link, Not a Copy)")
st.code('''copy_wrong = original
copy_wrong.append(4)
print(original)  # Output: [1, 2, 3, 4] (Original changed!)''', language="python")

st.success("✅ Correct:")
st.code('''copy_correct = original.copy()
copy_correct.append(5)
print(original)  # Output: [1, 2, 3] (Original unchanged)''', language="python")

st.subheader("💡 Summary Table")
st.table({
    "Operation": ["Create List", "Indexing", "Slicing", "Modify List", "Concatenate (+)", "Append (append())", "Extend (extend())",
                  "Remove Item (remove())", "Remove by Index (pop())", "Sort List (sort())", "Reverse List (reverse())",
                  "Loop (for)", "Zip Multiple Lists"],
    "Example": ["nums = [1, 2, 3]", "nums[0]", "nums[1:3]", "nums[1] = 100", "[1, 2] + [3, 4]", "nums.append(4)", "nums.extend([5, 6])",
                "nums.remove(2)", "nums.pop(1)", "nums.sort()", "nums.reverse()", "for x in nums: print(x)", "zip([1,2], ['a','b'])"],
    "Output": ["[1, 2, 3]", "1", "[2, 3]", "[1, 100, 3]", "[1, 2, 3, 4]", "[1, 2, 3, 4]", "[1, 2, 3, 4, 5, 6]",
               "[1, 3, 4, 5, 6]", "[1, 4, 5, 6]", "[1, 4, 5, 6]", "[6, 5, 4, 1]", "Prints each item", "(1, 'a'), (2, 'b')"]
})

st.write("This concludes the Python summary. Happy coding! 🚀")
