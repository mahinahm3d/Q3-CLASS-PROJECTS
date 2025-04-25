def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  

    # The sequence \033[1;3m \033[0m is an ANSI escape code used for text formatting in terminal output.
def bold_italic(text):
    return f"\033[1;3m{text}\033[0m"  

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)  
    
    
    print(f"{bold_italic(fahrenheit)}F is equal to {bold_italic(f'{celsius:.4f}')}C")

if __name__ == "__main__":
    main()