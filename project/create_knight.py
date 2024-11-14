import random

def create_knight(knights):
    knights_data= []
    print("Lets create a knight")
    knights_data.append(input("Enter the knight's name: "))
    knights.append(knights_data)


def change_data(knights):
    print("What would you like to update ? ")
    print("1.Knight's name: "+ knights[0])
    try:
        selection = int(input("Enter your option:"))
        if selection == 1:
            if knights_num == 0 :
                print("you have a knight")
            knights[0] = input("Whats knight's new name:")
            print("New Knight's name is: " + knights[0])
            return
        else:
            print("--- Please select a valid soption ---")
    except:
        print("--- try again! ---")
        change_data(knights)


def select_knight(knights):
    knights_num = 0
    print("What knight would you like to update?")
    while knights_num < len(knights):
        print(str(knights_num + 1) + "- knights name: "+ str(knights[knights_num][0]))
        knights_num += 1

    selection = (int(input("Select the knights number: "))-1)
    change_data(knights[selection])


def menu(knights_num):

    # Print the display options
    print("What would you like to do?")
    print("1.Create a new knight")
    print("2.Update your knight")
    print("0.Exit")
    
    # Allows a selection to be tested
    try:
        # Takes the users selection option
        select = int(input("Enter your selection: "))
        print()

        if select == 1:
            create_knight(knights)

            print("\n--- your knight ---\n")
            print("Knights name:"+ str(knights[knights_num][0]) + "\n")
            knights_num+=1
            menu(knights_num)

        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first!\n")
                #menu(knights)
            else:
                select_knight(knights)
            menu(knights_num)

        elif select == 0:
            print("--- All your knights ---\n")
            # Reset the knights_num to count all knights
            knights_num = 0
            while knights_num < len(knights):
                print(str(knights_num + 1) + "- knights name: "+ str(knights[knights_num][0]))
                knights_num += 1

            if len(knights) == 0:
                print("wait...you have no knights! Have a number:"+ str(random.randint(1,100)))

        # If selection entered is not integer
        else:
            print("\n--- Try again ---\n")
            menu(knights_num)

    # If selection entered is not integer
    except:
        print("\n--- Try again ---\n")
        menu(knights_num)

knights_num = 0
knights= [] 
# Run the program
menu(knights_num)