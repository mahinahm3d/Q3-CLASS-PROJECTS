import time

def mad_libs():
    print("Welcome to the Ultimate Mad Libs Adventure! Fill in the blanks below:\n")

    # user inputs
    name = input("Enter a name: ")
    animal = input("Enter a type of animal: ")
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    food = input("Enter a type of food: ")
    sound = input("Enter a funny sound (e.g., 'Boing', 'Zzzz', 'Splork'): ")
    number = input("Enter a number: ")
    superhero = input("Enter a superhero name: ")
    silly_word = input("Enter a silly word (e.g., 'Blorp', 'Zizzle', 'Fluffernoodle'): ")
    vehicle = input("Enter a type of vehicle: ")
    emotion = input("Enter an emotion (e.g., 'Excited', 'Nervous', 'Confused'): ")

    # Creating the story
    story = f"""
    One fine morning, {name} woke up feeling {adjective1}. It was a perfect day to visit {place}, 
    so {name} put on their {adjective2} shoes and hopped onto their {vehicle}. 

    Just as they arrived, a {animal} wearing sunglasses ran past them, shouting "{silly_word}!!" 
    Confused, {name} decided to {verb1} after it. But before they could catch up, a giant {food} 
    fell from the sky, making a loud '{sound}!' SPLAT! Right on top of {name}!

    Covered in {food}, {name} felt {emotion}. But suddenly, a mysterious figure appeared... It was {superhero}!
    "{name}, you must save the world from the Evil {animal} Army!" {superhero} exclaimed.
    
    Without hesitation, {name} grabbed a {food} launcher and started to {verb2} towards the battle.
    It was an EPIC fight—{number} {animal}s against one determined {name}!

    In the end, {name} saved the day and was crowned the **Champion of {place}**. 
    Everyone chanted, "{silly_word}, {silly_word}!" as confetti rained down.

    And from that day on, {name} was known as the **Great {superhero} of {place}**!

    The End. 🎉😂
    """

    print("\nGenerating your EPIC Mad Libs story...\n")
    time.sleep(3)  # Adding a time effect
    print(story)
    


mad_libs()