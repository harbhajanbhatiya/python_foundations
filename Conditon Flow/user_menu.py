menu_option = ""
while menu_option != "q":
    print("\nMenu Options:")
    print("1. Add order amount to a running list")
    print("2. Show all orders and totals after applying discounts")
    print("q. Quit")
    menu_option = input("Select an option: ")
    if menu_option == "1":
        print("Adding order amount to running list...")
    elif menu_option == "2":
        print("Showing all orders and totals after applying discounts...")
    elif menu_option == "q":
        print("Quiting")
        break
    else:
        print("Invalid option. Please try again.")