import random

def choose_word():
    """Returns a random word from a predefined list."""
    words = ["python", "developer", "hangman", "challenge", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and others hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    """Main function to play Hangman."""
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman Game!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess!")
            attempts -= 1
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()