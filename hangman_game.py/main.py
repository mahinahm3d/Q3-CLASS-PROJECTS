import random
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from getpass import getpass
from datetime import datetime

console = Console()
history_file = "hangman_history.txt"

HANGMAN_PICS = [
    """\n\n\n\n\n\n""",
    """\n\n\n\n\n=====""",
    """\n |\n |\n |\n |\n=====""",
    """ +---+\n |\n |\n |\n |\n=====""",
    """ +---+\n |   |\n O   |\n     |\n     |\n=====""",
    """ +---+\n |   |\n O   |\n |   |\n     |\n=====""",
    """ +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n====="""
]

WORDS = ["python", "developer", "hangman", "challenge", "openai"]
score = {"wins": 0, "losses": 0}

def choose_word():
    choice = console.input("\n🔧 Choose word mode — [1] Random [2] Enter your own: ").strip()
    if choice == "2":
        word = getpass("🙈 Enter a secret word (no peeking): ").lower()
        if word.isalpha():
            return word
        else:
            console.print("❌ Invalid word. Using random instead.", style="bold red")
    return random.choice(WORDS)

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def print_game_state(word, guessed, attempts):
    console.clear()
    hangman_art = HANGMAN_PICS[6 - attempts]
    word_display = display_word(word, guessed)
    guessed_str = " ".join(sorted(guessed)) or "None yet"

    console.print(Panel(hangman_art, title="Hangman", border_style="red"))
    console.print(Text(f"\nWord: {word_display}", style="bold cyan"))
    console.print(Text(f"Guessed Letters: {guessed_str}", style="yellow"))
    console.print(Text(f"Attempts Left: {attempts}", style="green"))

def save_history(word, won):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    outcome = "Win" if won else "Loss"
    with open(history_file, "a") as f:
        f.write(f"{now} | {outcome} | Word: {word}\n")

def hangman():
    word = choose_word()
    guessed = set()
    attempts = 6

    console.print(Panel("🎮 Welcome to [bold magenta]Hangman[/bold magenta]!", style="bold blue"))

    while attempts > 0:
        print_game_state(word, guessed, attempts)
        guess = console.input("\n🔤 Guess a letter: ").lower()

        if not is_valid_guess(guess):
            console.print("❗ Enter a single alphabetical letter.", style="bold red")
            continue

        if guess in guessed:
            console.print("⚠️ Already guessed that letter.", style="italic yellow")
            continue

        guessed.add(guess)

        if guess in word:
            console.print("✅ Good guess!", style="bold green")
            if all(letter in guessed for letter in word):
                print_game_state(word, guessed, attempts)
                console.print(f"\n🎉 [bold green]You won! The word was:[/bold green] {word}")
                score["wins"] += 1
                save_history(word, True)
                break
        else:
            console.print("❌ Wrong guess!", style="bold red")
            attempts -= 1
    else:
        print_game_state(word, guessed, attempts)
        console.print(f"\n💀 [bold red]You lost. The word was:[/bold red] {word}")
        score["losses"] += 1
        save_history(word, False)

    console.print(f"\n📊 [bold magenta]Scoreboard:[/bold magenta] {score['wins']} Wins | {score['losses']} Losses", style="bold cyan")
    again = console.input("\n🔁 Play again? (y/n): ").lower()
    if again == 'y':
        hangman()
    else:
        console.print("\n👋 Thanks for playing!", style="bold blue")

if __name__ == "__main__":
    hangman()
