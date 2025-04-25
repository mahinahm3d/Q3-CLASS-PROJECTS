import random

NUM_SIDES: int = 6

def roll_dice():
   
    print("Dice have", NUM_SIDES, "sides each.")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    roll_dice()