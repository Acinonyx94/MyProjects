#A shopping list program which gives users the choice to modify their shopping lists as either a STACK or QUEUE

shopping = ["potato", "bread", "juice", "eggs"]

#This function provides the functionality to treat the shopping list as a STACK
def shopping_stack():
    menu_choice = input("Select an Option\n1. Push\n2. Pop\n3. View\n4. Quit\n")
    if menu_choice == "1":
        pushed_item = input("Enter an item to add to the shopping list\n")
        shopping.append(pushed_item)
    elif menu_choice == "2":
        shopping.pop()
    elif menu_choice == "3":
        print(shopping)
    elif menu_choice == "4":
        print("Your order is on its way!")
        return
    else:
        print("Invalid Option")
        shopping_stack()
    shopping_stack()

#This function provides functionality for a QUEUE
def shopping_queue():
    menu_choice = input("Select an Option\n1. Push\n2. Pop\n3. View\n4. Quit\n")
    if menu_choice == "1":
        pushed_item = input("Enter an item to add to the shopping list\n")
        shopping.append(pushed_item)
    elif menu_choice == "2":
        shopping.pop(0)
    elif menu_choice == "3":
        print(shopping)
    elif menu_choice == "4":
        print("Your order is on its way!")
        return
    else:
        print("Invalid Option")
        shopping_queue()
    shopping_queue()

#This is the parent function and presents the initial menu for the program.
def shopping_list():
    q_or_stack = input("Would you like a queue (q) or a stack (s)?\n")
    if q_or_stack == "q":
        shopping_queue()
    elif q_or_stack == "s":
        shopping_stack()
    else:
        print("Invalid input")
        shopping_list()

shopping_list()