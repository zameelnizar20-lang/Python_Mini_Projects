import winsound
import time 

def countdown(seconds):
    while seconds > 0:
        mins , secs = divmod(seconds, 60)
        output = f"{mins:02d} : {secs:02d}"
        print(output,end="\r")
        winsound.Beep(1000,500)
        time.sleep(1)
        seconds -= 1


countdown(10)