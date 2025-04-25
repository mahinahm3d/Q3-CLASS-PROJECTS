def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    while True:
        print("\nOperations: 1. Access  2. Modify  3. Slice  4. Exit")
        choice = input("Choose an operation: ")

        if choice == '1':
            index = int(input("Enter index: "))
            if 0 <= index < len(my_list):
                print(f"Element at index {index}: {my_list[index]}")
            else:
                print("Invalid index.")

        elif choice == '2':
            index = int(input("Enter index: "))
            if 0 <= index < len(my_list):
                new_value = input("Enter new value: ")
                my_list[index] = new_value
                print("Updated list:", my_list)
            else:
                print("Invalid index.")

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            if 0 <= start <= end <= len(my_list):
                print("Sliced list:", my_list[start:end])
            else:
                print("Invalid range.")

        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose between 1-4.")

if __name__ == "__main__":
    main()