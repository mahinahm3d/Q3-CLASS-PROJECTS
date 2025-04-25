import random

def guess_the_number():
    print("🎮 Welcome to 'Guess the Number'! 🎮")
    print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

    secret_number = random.randint(1, 100)  # Computer picks a random number
    attempts = 0  # Counter for attempts

    while True:
        try:
            guess = int(input("Enter your guess: "))  # user input
            attempts += 1  # Increment attempts

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts! 🎉")
                print(f"Made ❤ by Asiya Khan")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Oops! Please enter a valid number.")


guess_the_number()