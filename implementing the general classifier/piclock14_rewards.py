import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

'''
setmode = BOARD
INPUTS : 11, 13, 15
OUTPUTS: 36, 38, 40
CLOCK  : 7
REWARD (-): 35
REWARD (+): 37

my_pwm.start(50) to start the analog signal at 50%
my_pwm.ChangeDutyCycle(1) to change the analog signal to 1%
my_pwm.ChangeFrequency(1000) to change the Hz
my_pwm.stop() to stop the signal, but kills the loop
'''

GPIO.setwarnings(False)    # Ignore warnings
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

# - Set the clock:
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

# - Set the reward PINs:
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

# - Initiate the analog objects:
my_pwm_negative = GPIO.PWM(35,1000)  # (pin, Hz)
my_pwm_positive = GPIO.PWM(37,1000)  # (pin, Hz)

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
        
        # - Reward:
        reward = input("Set the reward (0 < r < 100): ")
        my_pwm_negative.start(reward)
        my_pwm_positive.start(reward)
        print("- Transmitting", reward)
        sleep(5)
        
        # - Stop:
        my_pwm_negative.start(0)
        my_pwm_positive.start(0)
  
except:
    print(" ")
    print("Cleaning GPIO and exiting...")
    GPIO.cleanup()
    print("Done!")
