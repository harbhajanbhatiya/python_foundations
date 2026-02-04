def add_price(prices_list,price): 
    prices_list.append(price)
    print(f"Price {price} added.")
def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)
def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None
    return max(prices_list)

def menu():
    prices = []
    while True:
        print("\nMenu:")
        print("1. Add Price")
        print("2. Get Average Price")
        print("3. Get Max Price")
        print("q. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            price = float(input("Enter price to add: "))
            add_price(prices, price)
        elif choice == '2':
            avg_price = get_average_price(prices)
            print(f"Average Price: {avg_price}")
        elif choice == '3':
            max_price = get_max_price(prices)
            if max_price is not None:
                print(f"Max Price: {max_price}")
            else:
                print("No prices available.")
        elif choice.lower() == 'q':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")
    
menu()