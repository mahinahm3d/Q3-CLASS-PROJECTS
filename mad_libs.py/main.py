import time
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

def validate_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def mad_libs():
    # Title banner
    banner = pyfiglet.figlet_format("Mad Libs Fun!")
    print(Fore.CYAN + banner)

    print(Fore.YELLOW + "Welcome to the Ultimate Mad Libs Adventure! Fill in the blanks below:\n")

    # User inputs with validation
    name = input(Fore.GREEN + "Enter a name: ")
    animal = input(Fore.GREEN + "Enter a type of animal: ")
    place = input(Fore.GREEN + "Enter a place: ")
    adjective1 = input(Fore.GREEN + "Enter an adjective: ")
    verb1 = input(Fore.GREEN + "Enter a verb: ")
    sound = input(Fore.GREEN + "Enter a funny sound (e.g., 'Boing', 'Zzzz', 'Splork'): ")
    number = validate_number(Fore.GREEN + "Enter a number: ")
    vehicle = input(Fore.GREEN + "Enter a type of vehicle: ")
    emotion = input(Fore.GREEN + "Enter an emotion (e.g., 'Excited', 'Nervous', 'Confused'): ")

    # Creating the story
    story = f"""
    One fine morning, {name} woke up feeling {adjective1}. It was a perfect day to visit {place}, 
    so {name} hopped onto their {vehicle} and drove off.

    As they were cruising, a {animal} appeared, making a funny noise: "{sound}!" 
    Surprised, {name} decided to {verb1} after it. But suddenly, a giant {animal} appeared out of nowhere, 
    and {name} realized it was {number} times bigger than the first one!

    Feeling {emotion}, {name} hit the gas and zoomed away, narrowly escaping the creature.

    The End. 🎉
    """

    print(Fore.MAGENTA + "\nGenerating your EPIC Mad Libs story...\n")
    time.sleep(2)  # Adding a time effect
    print(story)

mad_libs()
