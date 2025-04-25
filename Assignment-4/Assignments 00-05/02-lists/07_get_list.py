# Program to take user input continuously until an empty input is given

def get_user_list():
    user_list = []
    
    while True:
        element = input("Enter a value: ")
        if element == "":
            break
        user_list.append(element)
    
    print("Here's the list:", user_list)

if __name__ == "__main__":
    get_user_list()