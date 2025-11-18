import os
import datetime
import time


alarm_input = input("Please Input the Time as ('HH:MM') Like this : ")

try :
    alarm_hours, alarm_mins = map(int, alarm_input.split(":"))
    if not (0<= alarm_hours <= 23 and 0 <= alarm_mins <= 59):
        raise ValueError
        
except ValueError:
    print("Invalid time format! Please enter in HH:MM format (e.g. 07:30 or 19:45).")

now = datetime.datetime.now()
alarm_time  = datetime.datetime.combine(now.date() , datetime.time(alarm_hours ,alarm_mins))


if alarm_time <= now:
    alarm_time += datetime.timedelta(days=1)

print(f"✅ Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M')} — waiting...")

# Step 4: Wait loop
try:
    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print("\n⏰ WAKE UP! It's time!")
            # Step 5: Play alert sound (simple terminal beep)
            for _ in range(5):
                print('\a')  # Beep sound (works in most terminals)
                time.sleep(1)
            # Optional: open sound file or system beep
            # os.system("start alarm.mp3")  # Windows
            break
        # Sleep a bit to avoid busy loop
        time.sleep(20)
except KeyboardInterrupt:
    print("\nAlarm cancelled by user.")