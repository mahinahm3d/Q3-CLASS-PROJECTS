import random

def computer_guesses():
    print("💭 Think of a number between 1 and 100, and I will try to guess it!")
    print("Enter 'H' if my guess is too high, 'L' if it's too low, and 'C' if I guessed correctly.\n")

    low, high = 1, 50
    attempts = 0

    while True:
        # Computer guess a number
        guess = random.randint(low, high)
        attempts += 1
        print(f"🤖 My guess is: {guess}")

        # user feedback
        feedback = input("Is my guess (H)igh, (L)ow, or (C)orrect? ").strip().upper()

        if feedback == "H":
            high = guess - 1  
        elif feedback == "L":
            low = guess + 1  
        elif feedback == "C":
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts! 🎉")
            print(f"Made ❤ by Asiya Khan")
            break
        else:
            print("❌ Invalid input! Please enter 'H', 'L', or 'C'.")


computer_guesses()