import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    
    print("🎮 Welcome to Rock, Paper, Scissor Game! 🎮")
    
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: Rock, Paper, or Scissors (or type 'exit' to quit)")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == "exit":
            print("\n🏆 Final Score:")
            print(f"👤 You: {user_score} | 🤖 Computer: {computer_score}")
            print("Thanks for playing! 👋")
            break

        if user_choice not in choices:
            print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")

        
        if user_choice == computer_choice:
            print("😲 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

play_rps()