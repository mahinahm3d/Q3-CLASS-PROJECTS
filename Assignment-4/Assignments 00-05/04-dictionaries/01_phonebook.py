def phonebook_app():
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    for name, number in phonebook.items():
        print(f"{name} -> {number}")
    
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])
        else:
            print(f"{name} is not in the phonebook.")

if __name__ == "__main__":
    phonebook_app()