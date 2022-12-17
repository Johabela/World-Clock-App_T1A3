from os import system
from cities import *
import pytz
from simple_term_menu import TerminalMenu
from pytz import timezone
from datetime import datetime, time 

def main():

        only_cities = ["Sydney","Bogota", "Auckland ","Berlin", "London", "Rome","Tokyo"]

# Displaying a list of cities into Menu 2

        Menu_2 = TerminalMenu(only_cities)
        Menu_2.show()

# Saving City 1 
        # city_1 = list_of_cities [Menu_2.chosen_menu_index]

# Matching cities from the Menu 2 with the nested dictionary 

        # print(list_of_cities [Menu_2.chosen_menu_index]["city"])


# Displaying Time Zone date and current time City 1 

        # time_zone_1 = pytz.timezone(city_1["timezone"])
        # local_time_1=datetime.now(time_zone_1)
        # current_time_1=local_time_1.strftime("%a %x %H:%M:%S")

        # print(time_zone_1)
        # print(current_time_1)