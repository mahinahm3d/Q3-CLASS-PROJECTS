def shorten(lst):
    REMOVE_COUNT = 2 if len(lst) % 2 == 0 else 2  
    
    for _ in range(min(REMOVE_COUNT, len(lst))):
        removed_element = lst.pop()  
        print("Removed:", removed_element)
    
    print("Shortened list:", lst)

def get_user_list():
    while True:
        num_elements = int(input("Enter the number of elements in the list (min 3, max 50): "))
        if 3 <= num_elements <= 50:
            break
        print("Invalid input! Please enter a number between 3 and 50.")
    
    user_list = []
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    print("Original list:", user_list)
    shorten(user_list)

if __name__ == "__main__":
    get_user_list()