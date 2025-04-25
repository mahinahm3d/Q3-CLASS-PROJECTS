import time

def main(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')  
        time.sleep(1)  
        seconds -= 1

    print("Go for a run now!!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the time in seconds: "))
        main(user_input)
    except ValueError:
        print("Please enter a valid integer.")