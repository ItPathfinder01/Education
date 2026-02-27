def main_menu():
    while True:
        order = get_order()
        print("Check the order")
        print_order(order)
        confirm = input("Is everything ok? To confirm the order press Y, to decline press N: ")
        if confirm == "Y" or confirm == "y":
            save_order(order)
            print("Thx for the order")
            print_order(order)
        else:
            continue

def get_order():
    return {}

def print_order(order):
    print(order)
    return

def save_order(order):
    print("Your order is saved")
    return

main_menu()


