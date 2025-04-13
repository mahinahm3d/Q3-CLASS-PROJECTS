import random
def computer_guesses_number():
    print("🧠 Welcome to 'Guess the Number (Computer Edition)'! 🤖")
    print("Think of a number in your mind, and I'll try to guess it!")

    while True:
        try:
            lower = int(input("Enter the lowest number in the range: "))
            upper = int(input("Enter the highest number in the range: "))
            if lower >= upper:
                print("⚠️ Lower bound must be less than upper bound.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter valid integers.")

    print(f"\nOkay! Think of a number between {lower} and {upper}, but don't tell me! 🤫")
    input("Press Enter when you're ready...")

    attempts = 0
    while lower <= upper:
        guess = (lower + upper) // 2
        attempts += 1
        print(f"\n🤔 Is your number {guess}?")
        response = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ").strip().lower()

        if response == 'h':
            upper = guess - 1
        elif response == 'l':
            lower = guess + 1
        elif response == 'c':
            print(f"\n🎉 Yay! I guessed your number {guess} in {attempts} attempts! 🏆")
            break
        else:
            print("⚠️ Invalid response. Please enter 'h', 'l', or 'c'.")

    else:
        print("😕 Hmm... something doesn't add up. Were you honest with your answers?")

    # Replay?
    replay = input("\n🔁 Want to play again? (yes/no): ").strip().lower()
    if replay in ('yes', 'y'):
        print("\n🔄 Restarting the game...\n")
        computer_guesses_number()
    else:
        print("\n💖 Thanks for playing! Made with ❤ by Mahin Ahmed. Bye-bye!")

# Run the game
computer_guesses_number()
