def divide_numbers():
    
    try:
        num1 = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))
        num2 = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        quotient = num1 // num2
        remainder = num1 % num2
        print(f"The result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    divide_numbers()