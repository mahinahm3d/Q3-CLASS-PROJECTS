# countdown_timer.py
# A simple command-line countdown timer with support for mm:ss input.
# Last updated: April 2025

import time
import sys
import os

def beep():
    """Cross-platform beep sound."""
    try:
        # Windows
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 500)
        else:
            # macOS and Linux (may need terminal support)
            print('\a', end='', flush=True)
    except:
        pass  # Fails silently if beep not supported

def parse_input(user_input: str) -> int:
    """Parses 'mm:ss' or 'ss' into total seconds."""
    parts = user_input.strip().split(":")
    if len(parts) == 1:
        return int(parts[0])
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds
    else:
        raise ValueError("Invalid time format.")

def countdown_timer(seconds: int):
    if seconds <= 0:
        print("Please enter a positive time.")
        return

    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r", flush=True)
        time.sleep(1)
        seconds -= 1

    print("\nGo for a run now!!")
    beep()

if __name__ == "__main__":
    try:
        user_input = input("Enter time (mm:ss or ss): ")
        total_seconds = parse_input(user_input)
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid time like '90' or '1:30'.")
