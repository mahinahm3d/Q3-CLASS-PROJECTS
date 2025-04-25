import math

def calculate_hypotenuse():
    
    try:
        a = float(input("Enter the length of AB: "))
        b = float(input("Enter the length of AC: "))
        hypotenuse = math.sqrt(a**2 + b**2)
        print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_hypotenuse()