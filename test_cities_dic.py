def cities():
 list_of_cities = [
    {"city": "Sydney", "timezone": "Australia/Sydney"},
    {"city": "Bogota", "timezone": "America/Bogota"},
    {"city": "Auckland", "timezone": "Pacific/Auckland"},
    {"city": "Berlin", "timezone": "Europe/Berlin"},
    {"city": "London", "timezone": "Europe/London"},
    {"city": "Rome", "timezone": "Europe/Rome"},
    {"city": "Tokyo", "timezone": "Asia/Tokyo"},
    ]
 list_of_current_cities = [list_of_cities]
 return list_of_current_cities

city=cities()

def test_1():
    assert city[2]["city"]!= "Auckland"
