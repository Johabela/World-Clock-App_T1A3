from os import system
from cities import *
import pytz
from simple_term_menu import TerminalMenu
from pytz import timezone
from datetime import datetime, time 

print()
print("This is the World Clock App")
print()
print("What would you like to do?")

# 1st Feature-------Creating function  Menu_1  ---------------------------------------------------------
def options_menu1():
    print("1. See the current time in two cities")
    print("2. Predicting the time in multiple cities")
    print("3. Exit")
    user_selection = input ("Select options from (1-3): ")
    return user_selection


selection = ""
city_1 = ""
city_2 = ""

# 1st Feature----While loop Menu 1 , that it is part of the 1st Feature ---------------------------------
while selection != "3":
    selection = options_menu1()
    if selection == "1":
        system("clear")
        print("Welcome to see the current time in two different Cities in the world!")
        print()
        print("Select The City Number One: ")
        

        # 2st Feature --------Creating Menu 2 using Simple_Terminal_ Menu package ------------------------
        only_cities = ["Sydney","Bogota", "Auckland ","Berlin", "London", "Rome","Tokyo"]

        # Displaying a list of cities into Menu 2 --------------------------------------------------------
        Menu_2 = TerminalMenu(only_cities)
        Menu_2.show()


        # Saving City 1 ----------------------------------------------------------------------------------
        city_1 = list_of_cities [Menu_2.chosen_menu_index]


        # 3st Feature ---------Displaying Time Zone date and current time City 1 -------------------------
        time_zone_1 = pytz.timezone(city_1["timezone"])
        local_time_1=datetime.now(time_zone_1)
        current_time_1=local_time_1.strftime("%a %x %H:%M:%S")
        print(time_zone_1)
        print(current_time_1)
        print()

        # 2st Feature --------Creating Menu 3 using Simple_Terminal_ Menu package ------------------------
        print("Select The City Number Two:")
        Menu_3 = TerminalMenu(only_cities)
        Menu_3.show()

        # Saving City 2 ----------------------------------------------------------------------------------
        city_2 = list_of_cities [Menu_3.chosen_menu_index]
        
        # 3st Feature ---------Displaying Time Zone date and current time City 2-------------------------
        time_zone_2 = pytz.timezone(city_2["timezone"])
        local_time_2 = datetime.now(time_zone_2)
        current_time_2 = local_time_2.strftime("%a %x %H:%M:%S")
        print(time_zone_2)
        print(current_time_2)
        print()

        # Saving City 1 ----------------------------------------------------------------------------------
        city_2 = list_of_cities [Menu_3.chosen_menu_index]

#  
        # 4th Feature ----Calculate and displaying the time difference between City 1 & City 2 -----------
        time_difference = int (local_time_1.strftime ("%z"))
        time_difference_1 = int(local_time_2.strftime ("%z"))
        if (time_difference > time_difference_1):
            print("Time difference between", (city_1["city"]), "and", (city_2["city"]), "is", 
            (time_difference-time_difference_1) /100, "hours")

        
        # Taking in consideration if the cities don't have time difference --------------------------------
        elif(time_difference == time_difference_1):
            print("There is not time difference!")
            
    #5th Feature Pending ----------------------------------------------------------------------------------
    # Predicting the time the user would like to see and schedule/save it in the calendar  
    elif selection == "2":
        print ("Predicting Time Zone in progress")

    # Exit option , user will end the program -------------------------------------------------------------
    elif selection == "3": 
        continue 

    # Continuing the loop until exit or press any key to go back to the main menu --------------------------------
    else: 
        print ("Invalid option")
    input ("press any key to go back to the main menu")
    system("clear")
 
