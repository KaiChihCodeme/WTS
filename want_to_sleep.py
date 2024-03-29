from pynput.mouse import Controller
import sys
import signal
import time

def signal_handler(sig, frame):
    if sig == signal.SIGINT.value:
        print('You are waked up!')
        sys.exit(0)

# register signal handler
signal.signal(signal.SIGINT, signal_handler)

command = input("Are you want to start sleeping? (Y/N)")
if (command == "Y" or command == "y"):
    period = int(input("How many seconds to sleep? (min)"))

    mouse = Controller()
    # Set Initial Position of mouse
    mouse.position = (10, 20)

    while (period != 0):
        # move every minute
        print("Sleeping..." + "remaining mins" + str(period))
        mouse.move(100, 100)
        time.sleep(1)
        mouse.move(-100, -100)
        time.sleep(60)
        period -= 1
else:
    print("Why you are here?")
    sys.exit(0)