import time
import pygame

def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")  # Replace "alarm_sound.mp3" with the path to your alarm sound file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! It's time to wake up!")
            play_alarm()
            break
        time.sleep(1)

def main():
    print("Enter the time for the alarm in HH:MM:SS format:")
    alarm_time = input()

    try:
        time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    print(f"Alarm set for {alarm_time}")

    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
