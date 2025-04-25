def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

if __name__ == "__main__":
    message = input("Enter a message to copy: ")
    
    my_list = []
    print("List before:", my_list)
    
    add_three_copies(my_list, message)
    
    print("List after:", my_list)