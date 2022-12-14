from pytz import timezone
from datetime import datetime
import time 
import pytz


city_country_1 = pytz.timezone("Australia/Sydney")
local_time_1=datetime.now(city_country_1)
current_time_1=local_time_1.strftime("%a %x %H:%S")
print(city_country_1)
print(current_time_1)


city_country_2 = pytz.timezone("America/Bogota")
local_time_2=datetime.now(city_country_2)
current_time_2=local_time_2.strftime("%a %x %H:%S")
print(city_country_2)
print(current_time_2)