def feet_to_inches(feet):
    
    return feet * 12

def main():
    try:
        feet = float(input("Enter number in feet: "))
        inches = feet_to_inches(feet)
        unit = "foot" if feet == 1 else "feet"
        print(f"That is {inches} inches!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()