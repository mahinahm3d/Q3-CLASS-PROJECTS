def fruit_shop():
    fruits = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 7.5,
        "rambutan": 12.0,
        "mango": 18.5
    }
    
    total_cost = 0
    
    for fruit, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    fruit_shop()