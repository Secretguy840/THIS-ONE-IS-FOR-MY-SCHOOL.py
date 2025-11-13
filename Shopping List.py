# List methods
shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to list!")
    
    elif choice == '2':
        if shopping_list:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from list!")
            else:
                print("Item not found!")
        else:
            print("List is empty!")
    
    elif choice == '3':
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("Your list is empty!")
    
    elif choice == '4':
        print("Thank you for using Shopping List!")
        break
    
    else:
        print("Invalid choice! Please try again.")
