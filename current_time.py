from datetime import datetime
import pytz 
from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)
    print()

