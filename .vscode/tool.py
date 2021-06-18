import keyboard

messages = 0
deleted = 0
pressed = False

try: 
    while True:
        if keyboard.is_pressed('ctrl+shift'): # may be changed on preference
            if not pressed:
                messages += 1
                print(f"Messages Sent: {messages}")
                pressed = True # prevents duplicates
        elif keyboard.is_pressed('ctrl+alt'): # second arg, may be changed on preference
            if not pressed:
                messages += 1
                deleted += 1 # sets deleted messages - which have a different value
                print(f"Messages Sent: {messages}\nDeleted Comments: {deleted}")
                pressed = True # prevents duplicates
        else:
            pressed = False # resets key press

except KeyboardInterrupt:
    print(f"Total Messages Sent: {messages}\nTotal Deleted Comments: {deleted}")

