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
output_F_vector = [0]*3
print(" ")
print("Define the 3 outputs (1 or 0):")
output_F_vector[0] = int(input("Output 1: "))
output_F_vector[1] = int(input("Output 2: "))
output_F_vector[2] = int(input("Output 3: "))


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
        sleep(2)
        
        # - CLOCK 1:
        # -- Set the clock to 1:
        GPIO.output(7,GPIO.HIGH)
        sleep(0.005) # 5ms delay: arduino delays 1ms for each output!
        
        # -- Measire the inputs:
        input_F_vector[0] = GPIO.input(36)
        input_F_vector[1] = GPIO.input(38)
        input_F_vector[2] = GPIO.input(40)
        print("INPUTS:")
        print(input_F_vector)
        
        # - Provide the reward (0 < r < 100):
        if input_F_vector == output_F_vector:
            my_pwm_negative.start(0)
            my_pwm_positive.start(100)
            reward = 100
        else:
            my_pwm_negative.start(100)
            my_pwm_positive.start(0)
            reward = 0

        print("- Transmitting", reward)
        sleep(2)
        
        # - Stop reward:
        my_pwm_negative.start(0)
        my_pwm_positive.start(0)
  
except:
    print(" ")
    print("Cleaning GPIO and exiting...")
    GPIO.cleanup()
    print("Done!")
