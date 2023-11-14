**Terminal App_T1A3**

[Github](https://github.com/Johabela/World-Work-App_T1A3)


___

**Code Style Guide**

I will follow [PEP8](https://peps.python.org/pep-0008/) Python Style Guide. 
___

**World Work Application**

 People struggle to organise catch-ups/ video calls online with family/ friends/ workmates based in other parts of the world. I personally do that's why I am creating this application called  World Clock App and it will have the following: 


**1st Feature - Menu**: 
- Main Menu (function & while loop). Users will be able to select  3 options within the app (1.Current, 2.Predict the time in two cities and 3.Exit)
    
**2nd Feature**:
- Current time zone has two Menus for Cities 1 and 2.

- There is a database called pytz in Python. I used it to bring the time zones and I created a main nested dictionaries in a list where I stored some cities names and timezones from pytz. 

- Instead of users typing the City, there are two menus created with a simple-terminal-menu, where the users can select the cities. This function had a list of some cities that will match with the main nested dictionary to bring the information needed. 

**3rd Feature** 
-Displaying current times of the cities selected, all of this is happening inside Current Time Zone section.   

- I worked with date time function and pytz time zones to match the cities select by the user displaying them on the terminal app. 

**4th Feature** 
- Calculates and displays the time difference between City 1 & City 2 selected by the user.

**5rd Feature**  
- Predicting Time Zones in multiple cities. This section is in progress. It will predict the time that the user would like to see in the future, the time will be saved and possible linked to a calendar.  

___

**Implementation Plan**


[Implementation Plan](https://docs.google.com/spreadsheets/d/1_rlFQfG0R0ZCxoQgWij7pDlmL0DQi3bk/edit?usp=sharing&ouid=103415341573224469400&rtpof=true&sd=true)

___

**Instructions to Run the app**

To be able to run the World Work App, you will need the install or have the following:

- [Python 3](https://www.python.org/)

- [pytz package](https://pypi.org/project/pytz/)

- [simple-term-menu 1.5.2](https://pypi.org/project/simple-term-menu/) only Linux and macOS are supported. 

- Datetime ans Os are Python's built-in modules, you won't need to install. 

- Activate the virtual environment with the command in the terminal -> source venv/bin/activate

- Run the Python script -> python cc_app.py
___


___
**Reference Sources** 

- Borislav Hadzhiev 2022, 'ModuleNotFoundError: No module named 'pytz' in Python', Bobbyhadz, web log post,20 April, viewed 10 December 2022, https://bobbyhadz.com/blog/python-no-module-named-pytz

- Borislav Hadzhiev 2022, 'TypeError: can only concatenate str (not "dict") to str', Bobbyhadz, web log post,20 April, viewed 10 December 2022,https://bobbyhadz.com/blog python-typeerror-can-only-concatenate-str-not-dict-to-str#:~:text=The%20Python%20%22TypeError%3A%20can%20only,specific%20key%20of%20the%20dictionary

- Chad Thackray 2022, Simple menus in python, online video, viewed 9 December,https://www.youtube.com/watch?v=Zpa-rc9e388


- edstem 2022, Coder Academy Content, viewed 14 December, https://edstem.org/au/courses/10081/lessons/27592/slides/194999

- John Nyingi 2019, Dev, Setting Up PEP8 and Pylint on VS Code,web log post ,viewed 8 December, https://dev.to/j0nimost/setting-up-pep8-and-pylint-on-vs-code-34h

- Kolade Chris, freecodecamp, How to Get the Current Time with the datetime Module, web log post, viewed 12 December, https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=You%20can%20get%20the%20current%20time%20in%20a%20particular%20timezone,with%20another%20module%20called%20pytz%20.&text=You%20can%20then%20check%20for,all%20timezones%20of%20the%20world 

- NeuralNine 2022, Handling Multiple Timezones in Python,
online video, viewed 8 December 2022, https://www.youtube.com/watch?v=lUe_-WnrPU

- pypi 2022, DateTime 4.8, pip install DateTime, web log post, viewed 14 December 2022, https://pypi.org/project/DateTime/

- pypi 2022, simple-term-menu 1.5.2, pip install simple-term-menu, web log post, viewed 9 December https://pypi.org/project/simple-term-menu/

- Python strftime cheatsheet 2021, Strftime, web log post,  viewed 9 December, https://strftime.org/ 

- Real Python 2022, Python's datetime Module and How Dates and Times are Messy,online video, viewed 11 December 2022, https://www.youtube.com/watch?v=lP2DqOduOv4

- Stuart Bishop 2022,*pip install pytz*, pytz 2022.6, web log post, 1 November, viewed 10 December 2022, https://pypi.org/project/pytz/

- The Grepper Developer Community 2020, codegrepper, ‘pytz timezones’ viewed 8 December 2022, https://www.codegrepper.com/tpc/pytz+timezones 

- Vikram Chiluka  2022, 'How to compare time in different time zones in Python?', tutorials point, web log post,15 September, viewed 14 December 2022, https://www.tutorialspoint.com/







