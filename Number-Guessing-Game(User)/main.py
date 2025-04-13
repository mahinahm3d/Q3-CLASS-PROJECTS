import time

def computer_guesses():
    print("💭 Think of a number between 1 and 100, and I will try to guess it!")
    print("📌 Respond with:")
    print("   'H' → My guess is too high")
    print("   'L' → My guess is too low")
    print("   'C' → My guess is correct\n")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\n🤖 Attempt #{attempts}: My guess is 👉 {guess}")
        feedback = input("Your response (H/L/C): ").strip().upper()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        elif feedback == "C":
            print(f"\n🎉 Woohoo! I guessed your number {guess} in {attempts} attempts!")
            print("🧠 Not bad for a machine, huh?")
            break
        else:
            print("❌ Invalid input. Please respond with H, L, or C.")
    else:
        print("\n😕 Something's not right. Are you sure you’re not changing your number mid-game?")
        print("🕵️ Ending game due to inconsistent feedback.")

    time.sleep(1)
    again = input("\n🔁 Wanna play again? (Y/N): ").strip().upper()
    if again == "Y":
        print("\n🔄 Restarting...\n")
        time.sleep(1)
        computer_guesses()
    else:
        print("\n👋 Thanks for playing! Made ❤️ by Mahin Ahmed.\n")


computer_guesses()
