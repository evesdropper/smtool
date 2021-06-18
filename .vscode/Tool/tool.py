import keyboard
import time
import timestat

# Setup
messages = 0
deleted = 0
msg_hk = 'ctrl+shift' # set keybinds 
del_hk = 'ctrl+alt'
pressed = False
start = time.time() # starts timer upon program running

# Tool 
try:
    while True:
        if keyboard.is_pressed(msg_hk): # keybind 1 - universal
            if not pressed:
                messages += 1
                print(f"Messages Sent: {messages}")
                pressed = True # prevents duplicates
        elif keyboard.is_pressed(del_hk): # keybind 2 - adds to total count and has separate count
            if not pressed:
                messages += 1
                deleted += 1 # sets deleted messages - which have a different value
                print(f"Messages Sent: {messages}\nDeleted Comments: {deleted}")
                pressed = True # prevents duplicates
        else:
            pressed = False # resets key press

except KeyboardInterrupt: # use CTRL+C to terminate program
    print(f"Total Messages Sent: {messages}\nTotal Deleted Comments: {deleted}") # Prints total message stats
    end = time.time() # time module
    print(f"Insights:\nTime Elapsed: {timestat.convert(start, end)}\nAverage Time per Message: {timestat.avg_time(int(end-start), messages)} seconds")
    
