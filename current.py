from pytz import timezone
from datetime import datetime
import time 
import pytz


# time_format = "%a-%d/%m/%y %H:%S"
# time_format = "%A %d %B %Y %H:%S"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>>>>

# print("Sydney Time")
# time_format = "%a %x %H:%S"
# now = datetime.now().strftime(time_format)
# print(now)

# print("Type a city or country you would to see the current time")
# print("Enter city/country where you are")

# user_input1 = input("Enter your city or country")
# if user_input1 == "Africa/Cairo" or "Africa/Johannesburg"or "America/Argentina/Buenos_Aires":
#      print(datetime.now(user_input1))
#      print(("%a %x %H:%S"))
# else:
#     print("sorry")
# city_country_2 =pytz. timezone ("America/Bogota")
# local_time=datetime.now(city_country_2)
# current_time=local_time.strftime("%a %x %H:%S")
# print(city_country_2)
# print(current_time)
    


# city_country_1 = pytz.timezone("Australia/Sydney")
# local_time=datetime.now(city_country_1)
# current_time=local_time.strftime("%a %x %H:%S")
# print(city_country_1)
# print(current_time)


city_country_1 = pytz.timezone("Australia/Sydney")
local_time_1=datetime.now(city_country_1)
current_time_1=local_time_1.strftime("%a %x %H:%S")
# print(city_country_1)
# print(current_time_1)


# city_country_2 = pytz.timezone("America/Bogota")
# local_time_2=datetime.now(city_country_2)
# current_time_2=local_time_2.strftime("%a %x %H:%S")
# print(city_country_2)
# print(current_time)


user_input1 = input("Enter your city or country")
if user_input1 == city_country_1:
    print(local_time_1)
    print(current_time_1)
else:
    print("sorry")