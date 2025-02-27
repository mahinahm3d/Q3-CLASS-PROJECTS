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
