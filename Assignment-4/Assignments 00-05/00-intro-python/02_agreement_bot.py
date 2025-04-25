def main():
    
    favorite_animal = input("What's your favorite animal? ")
    
    # The sequence \033[1;3m \033[0m is an ANSI escape code used for text formatting in terminal output.

    animal = f"\033[1;3m{favorite_animal}\033[0m"

    print(f"My favorite animal is also {animal}!")

if __name__ == "__main__":
    main()