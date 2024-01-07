import time

def countdown_timer(seconds):
    for remaining_time in range(seconds, 0, -1):
        minutes, seconds = divmod(remaining_time, 60)
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        print(f"Time left: {time_format}", end='\r')
        time.sleep(1)

    print("\nTime's up! Countdown complete.")

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter the countdown time in seconds: "))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Countdown Timer Program!")
    countdown_seconds = get_user_input()
    countdown_timer(countdown_seconds)

if __name__ == "__main__":
    main()
