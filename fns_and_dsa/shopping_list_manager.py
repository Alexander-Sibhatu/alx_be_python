

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip() # Prompt for and add an item
            if item:
                shopping_list.append(item)
                print(f"{item} is successfully added to the list")
            else:
                print("Invalid input.")
        elif choice == '2':
            item = input("Enter an item to remove") # Prompt for and remove an item
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} is successfully removed from the list")
            else:
                print(f"{item} is not found in the list")
        elif choice == '3':
            if shopping_list:
                print("\nShopping List") # Display the shopping list
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()