from os import system
import pytz
from simple_term_menu import TerminalMenu

print("Welcome to the World Clock App")

# Nesting dictionaries in a list 


list_of_cities = [
    {"city": "Sydney", "timezone": "Australia/Sydney"},
    {"city": "Bogota", "timezone": "America/Bogota"},
    {"city": "Auckland", "timezone": "Pacific/Auckland"},
    {"city": "Berlin", "timezone": "Europe/Berlin"},
    {"city": "London", "timezone": "Europe/London"},
    {"city": "New York", "timezone": "America/New_York"},
    {"city": "Los Angeles", "timezone": "America/Los_Angeles"},
]

def options_menu1():
    print("1. Current")
    print("2. Predicting time Zone")
    print("3. Exit")
    user_selection = input ("Select options from (1-3): ")
    return user_selection

selection = ""
city = ""

while selection != "3":
    selection = options_menu1()
    if selection == "1":
        system("clear")
        print("Select City number one")

        
        only_the_cities = []
        for city in list_of_cities:
            only_the_cities.append(city["city"])
        # options = ["Current Time Zone", "Predicting Time Zone", "Quit"]
            mainMenu = TerminalMenu(only_the_cities)
            mainMenu.show()
            # print("you select " + mainMenu.chosen_menu_entry)


        
    elif selection == "2":
        print ("welcome to predicting TZ")
    elif selection == "3": 
        continue 
    else: 
        print ("Invalid option")
    input ("press any key to continue")
    system("clear")
 



