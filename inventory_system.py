inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            if inventory[item_name] == 0:
                del inventory[item_name]
        else:
            print("Insufficient quantity to remove.")
    else:
        print("Item not found in inventory.")

def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def search_item(item_name):
    if item_name in inventory:
        print(f"{item_name} found in inventory with quantity {inventory[item_name]}.")
    else:
        print(f"{item_name} not found in inventory.")

def main():
    while True:
        print("\nInventory System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item_name, quantity)
            print("Item added to inventory.")
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(item_name, quantity)
            print("Item removed from inventory.")
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            item_name = input("Enter item name to search: ")
            search_item(item_name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
