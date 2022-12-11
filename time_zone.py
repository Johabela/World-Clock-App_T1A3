from datetime import datetime
import pytz 
# for tz in pytz.common_timezones:
#     print (tz)

#>>>>>>>>>>>>>>>>>>>>>Common timezones - I copied and pasted the main countries and cities into the list. 

# c_c_name = pytz.common_timezones ()

# c_c_time = datetime.now(c_c_name)
# print(c_c_time.strftime("Date is %a %x and time is %H:%S"))

#>>>>>>>>>>>>>>>>>>>>>> Getting the times zones of the selected cities and countries from the data base pytz 

c_c_Zones = [Africa/Cairo, Africa/Johannesburg, America/Argentina/Buenos_Aires, America/Argentina/Mendoza, 
America/Belize, America/Bogota, America/Cancun, America/Costa_Rica, America/Curacao, America/Detroit, America/El_Salvador, 
America/Guatemala, America/Havana, America, La_Paz, America/Lima, America/Los_Angeles, America/Managua, America/Mexico_City, 
America, New_York, America/Ojinaga, America/Panama, America/Porto_Velho, America/Puerto_Rico, America/Santiago, America/Sao_Paulo,
America/Tijuana, America/Toronto, America/Vancouver, Asia/Bangkok, Asia/Dubai, Asia/Gaza, Asia/Hebron, Asia/Hong_Kong, Asia/Jakarta, 
Asia/Jerusalem, Asia/Kuala_Lumpur, Asia/Makassar, Asia/Manila, Asia/Qatar, Asia/Seoul, Asia/Shanghai, Asia/Singapore, Asia/Tokyo, 
Australia/Adelaide, Australia/Brisbane, Australia/Darwin,Australia/Hobart, Australia/Melbourne, Australia/Perth, Australia/Sydney, 
Canada/Atlantic, Canada/Pacific, Europe/Amsterdam, Europe/Astrakhan, Europe/Athens, Europe/Berlin, Europe, Bratislava, Europe/Brussels, Europe/Budapest, Europe/Copenhagen, 
Europe/Dublin, Europe, Gibraltar, Europe/Guernsey, Europe/Helsinki, Europe/Istanbul, Europe/Kirov, Europe/Kyiv, Europe, 
Lisbon, Europe/London, Europe/Luxembourg, Europe/Madrid, Europe/Malta, Europe/Monaco, Europe/Moscow, Europe/Oslo, Europe/Paris, 
Europe/Prague, Europe/Rome, Europe/Stockholm, Pacific/Auckland, Pacific/Fiji, Pacific/Rarotonga, 
Pacific/Tahiti, US/Eastern, US/Hawaii, US/Mountain, US/Pacific, UTC]

