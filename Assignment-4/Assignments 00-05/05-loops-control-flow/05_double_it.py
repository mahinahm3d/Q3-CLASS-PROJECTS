def main():
    num = int(input("Enter a number: "))
    while num < 100:
        num *= 2
        print(num, end=" ")

if __name__ == "__main__":
    main()