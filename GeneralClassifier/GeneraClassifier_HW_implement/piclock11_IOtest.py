import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

'''
setmode = BOARD
INPUTS : 11, 13, 15
OUTPUTS: 36, 38, 40
'''

GPIO.setwarnings(False)    # Ignore warnings
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

# - Set the inputs (pulled low):
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# - Set the outputs to HIGH:
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)

# - Input F vector:
input_F_vector = [0]*3

try:
    while True:
        # - Measire the inputs:
        input_F_vector[0] = GPIO.input(36)
        input_F_vector[1] = GPIO.input(38)
        input_F_vector[2] = GPIO.input(40)

        # - Print the inputs:
        print(" ")
        print("Inputs:")
        print(input_F_vector)
        sleep(1)

except:
    print(" ")
    print("Cleaning GPIO...")
    GPIO.cleanup()
    print("Done!")