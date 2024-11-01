import datetime
import time

def set_alarm(hour, minute):
    # Get the current system time
    current_time = datetime.datetime.now()

    # Create a datetime object for the alarm time
    alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # Print the alarm time
    print("Alarm set for:", alarm_time.strftime("%H:%M"))

    # Calculate the time difference until the alarm
    time_difference = (alarm_time - current_time).total_seconds()

    # Pause execution until the alarm time is reached
    time.sleep(time_difference)

    # Print a message when the alarm goes off
    print("Alarm! Wake up!")

if name == "main":
    # Set the alarm time (hour and minute)
    alarm_hour = 8
    alarm_minute = 0

    # Call the set_alarm function
    set_alarm(alarm_hour, alarm_minute)