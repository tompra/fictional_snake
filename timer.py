import time
import pygame

def play_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("/Users/tom/Desktop/proyects/fictional_snake/audio/mixkit-interface-hint-notification-911.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Error playing sound: {e}")

def countdown(mins, secs, total_reps):
    for i in range(total_reps):
        total_time = mins * 60 + secs
        while total_time:
            remaining_mins, remaining_secs = divmod(total_time, 60)
            timer = '{:02d}:{:02d}'.format(remaining_mins, remaining_secs)
            print(f"Time left: {timer} - Session: {i + 1}/{total_reps}", end='\r')
            time.sleep(1)
            total_time -= 1
        print(f'\nTimer completed for session {i + 1}/{total_reps}')
        play_sound()

        if (i + 1) % 2 == 0 and (i + 1) != total_reps:
            take_short_break = input('Take a short break of 5 minutes? (yes/no): ').lower()
            if take_short_break == 'yes':
                countdown(5, 0, 1)
        elif (i + 1) % 5 == 0 and (i + 1) != total_reps:
            take_long_break = input('Take a longer break of 15 minutes? (yes/no): ').lower()
            if take_long_break == 'yes':
                countdown(15, 0, 1)

def user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print('Please enter a positive integer')
        except ValueError:
            print('Please enter a valid integer')

def main():
    minutes = user_input('Enter the number of minutes: ')
    seconds = user_input('Enter the number of seconds: ')
    repetitions = user_input('Enter the number of sessions: ')
    countdown(minutes, seconds, repetitions)

if __name__ == "__main__":
    main()
