# menu package

from simple_term_menu import TerminalMenu

#adding package simple terminal menu 

options = ["Current Time Zone", "Predicting Time Zone", "Quit"]

mainMenu = TerminalMenu (options)

mainMenu.show()

print("Choose any of the countries/cities below ")

# def options():
#     print("Australia/Sydney")
#     print("2. Predicting time Zone")
#     print("3. Exit")
#     user_selection = input ("Select options from (1-3): ")
#     return user_selection

# selection = ""

# while selection != "3":
#     selection = options()
#     if selection == "1":
#         print("welcome to current TZ")
#     elif selection == "2":
#         print ("welcome to predicting TZ")
#     elif selection == "3": 
#         continue 
#     else: 
#         print ("Invalid option")
#     input ("press any key to continue")
#     system("clear")
 

# city_country_1 = pytz.timezone("Australia/Sydney")
# local_time_1=datetime.now(city_country_1)
# current_time_1=local_time_1.strftime("%a %x %H:%S")
# # print(city_country_1)
# # print(current_time_1)


# user_input1 = input("Enter your city or country")
# if user_input1 == city_country_1:
#     print(local_time_1)
#     print(current_time_1)
# else:
#     print("sorry")
