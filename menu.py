from os import system
import pytz
from simple_term_menu import TerminalMenu
from pytz import timezone
from datetime import datetime
import time 

print("Welcome to the World Clock App")

# Nesting dictionaries in a list 

list_of_cities = [
    {"city": "Sydney", "timezone": "Australia/Sydney"},
    {"city": "Bogota", "timezone": "America/Bogota"},
    {"city": "Auckland", "timezone": "Pacific/Auckland"},
    {"city": "Berlin", "timezone": "Europe/Berlin"},
    {"city": "London", "timezone": "Europe/London"},
    {"city": "Rome", "timezone": "Europe/Rome"},
    {"city": "Tokyo", "timezone": "Asia/Tokio"},
]

# Creating Menu_1

def options_menu1():
    print("1. Current")
    print("2. Predicting time Zone")
    print("3. Exit")
    user_selection = input ("Select options from (1-3): ")
    return user_selection

selection = ""
city_1 = ""
city_2 = ""

# While loop Menu 1

while selection != "3":
    selection = options_menu1()
    if selection == "1":
        system("clear")
        print("Welcome to see the current time in two different Cities!")
        print()

        print("Select The City Number One: ")
        

# Creating Menu 2 using Simple_Terminal_ Menu package 
        only_cities = ["Sydney","Bogota", "Auckland ","Berlin", "London", "Rome","Tokyo"]

# Displaying a list of cities into Menu 2

        Menu_2 = TerminalMenu(only_cities)
        Menu_2.show()


# Saving City 1 
        city_1 = list_of_cities [Menu_2.chosen_menu_index]

# Matching cities from the Menu 2 with the nested dictionary 

        # print(list_of_cities [Menu_2.chosen_menu_index]["city"])


# Displaying Time Zone date and current time City 1 

        time_zone_1 = pytz.timezone(city_1["timezone"])
        local_time_1=datetime.now(time_zone_1)
        current_time_1=local_time_1.strftime("%a %x %H:%S")
        print(time_zone_1)
        print(current_time_1)

        print()


# Display Menu 2 again for users to select The City Number 2
        print("Select The City Number Two:")
        Menu_3 = TerminalMenu(only_cities)
        Menu_3.show()

# Saving City 2
        city_2 = list_of_cities [Menu_3.chosen_menu_index]

# Matching cities from the Menu 2 with the nested dictionary for The City 2
        # print(list_of_cities[Menu_3.chosen_menu_index]["city"])

# Displaying Time Zone date and current time City 2 

        time_zone_2 = pytz.timezone(city_2["timezone"])
        local_time_2=datetime.now(time_zone_2)
        current_time_2= local_time_2.strftime("%a %x %H:%S")
        print(time_zone_2)
        print(current_time_2)

        print()

# Saving City 2 
        city_2 = list_of_cities [Menu_2.chosen_menu_index]

    elif selection == "2":
        print ("welcome to predicting TZ")
    elif selection == "3": 
        continue 
    else: 
        print ("Invalid option")
    input ("press any key to go back to the main menu")
    system("clear")
 



