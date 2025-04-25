def get_user_list():
    num_elements = int(input("Enter the number of elements in the list: "))
    
    user_list = []
    
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    print("The last element in the list is:", user_list[-1])

if __name__ == "__main__":
    get_user_list()