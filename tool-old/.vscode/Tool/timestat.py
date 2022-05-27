import time 
import datetime

def convert(start_time, end_time):
    return str(datetime.timedelta(seconds = int(end_time) - int(start_time)))

def avg_time(elapsed, actions):
    return round(int(elapsed)/int(actions),3) if actions != 0 else "N/A"