from os import system

def options():
    print("1. Current time zone")
    print("2. Predicting time Zone")
    print("3. Exit")
    user_selection = input ("Select options from (1-3): ")
    return user_selection

selection = ""

while selection != "3":
    selection = options()
    if selection == "1":
        print("welcome to current TZ")
    elif selection == "2":
        print ("welcome to predicting TZ")
    elif selection == "3": 
        continue 
    else: 
        print ("Invalid option")
    input ("press any key to continue")
    system("clear")



