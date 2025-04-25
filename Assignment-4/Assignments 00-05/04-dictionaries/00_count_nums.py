from collections import defaultdict

def count_numbers():
    number_counts = defaultdict(int)
    
    while True:
        try:
            num = input("\033[94mEnter a number: \033[0m")
            if num == "":
                break
            num = int(num)
            number_counts[num] += 1
        except ValueError:
            print("Please enter a valid number.")
    
    for num, count in sorted(number_counts.items()):
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    count_numbers()