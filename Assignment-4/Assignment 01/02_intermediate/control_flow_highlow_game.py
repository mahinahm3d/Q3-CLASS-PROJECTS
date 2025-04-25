import random

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {your_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()

        if (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()