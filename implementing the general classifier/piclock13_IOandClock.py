import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

'''
setmode = BOARD
INPUTS : 11, 13, 15
OUTPUTS: 36, 38, 40
CLOCK  : 7
'''

GPIO.setwarnings(False)    # Ignore warnings
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

# - Set the clock:
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

# - Set the outputs with initial to LOW:
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

# - Set the inputs (pulled low):
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# - Input F vector:
input_F_vector = [0]*3

# - Output F vector:
output_F_vector = [1,0,1]

try:
    while True:
        print(" ")
        
        # - CLOCK 0:
        # -- Set the clock to 0:
        GPIO.output(7,GPIO.LOW)
        
        # -- Set the output vector:
        print("- OUPUT:")
        print(output_F_vector)
        if output_F_vector[0] == 1:
            GPIO.output(11,GPIO.HIGH)
        elif output_F_vector[0] == 0:
            GPIO.output(11,GPIO.LOW)
        if output_F_vector[1] == 1:
            GPIO.output(13,GPIO.HIGH)
        elif output_F_vector[1] == 0:
            GPIO.output(13,GPIO.LOW)
        if output_F_vector[2] == 1:
            GPIO.output(15,GPIO.HIGH)
        elif output_F_vector[2] == 0:
            GPIO.output(15,GPIO.LOW)
        sleep(1)
        
        # - CLOCK 1:
        # -- Set the clock to 1:
        GPIO.output(7,GPIO.HIGH)
        
        # -- Measire the inputs:
        input_F_vector[0] = GPIO.input(36)
        input_F_vector[1] = GPIO.input(38)
        input_F_vector[2] = GPIO.input(40)
        print("INPUTS:")
        print(input_F_vector)
        sleep(1)

  
except:
    print(" ")
    print("Cleaning GPIO...")
    GPIO.cleanup()
    print("Done!")
