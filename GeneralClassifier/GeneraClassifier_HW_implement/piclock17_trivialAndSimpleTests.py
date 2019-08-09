import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
import random

# - Parameters:
sleep_time = 1



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

print(" ")
print(" ")
print(" ")
print("TESTS:")
print("1. Trivial test:")
print("- Constant output=[1,0,1]")
print("- Correct answer(input)=[1,0,0]")
print(" ")
print("2. Simple test:")
print("- If output=[1,0,0], answer=[0,1,0]")
print("- If output=[0,1,0], answer=[1,0,0]")
test_type = int(input("Specify test (int): "))


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

# - Define the output:
if test_type == 1:
    output_F_vector[0] = 1
    output_F_vector[1] = 0
    output_F_vector[2] = 1


try:
    while True:
    
        print(" ")
        
        # - CLOCK 0:
        # -- Set the clock to 0:
        GPIO.output(7,GPIO.LOW)
        
        # - Define the output:
        if test_type == 2:
            rand_int = random.randint(0,1)
            if rand_int == 0:
                output_F_vector[0] = 1
                output_F_vector[1] = 0
                output_F_vector[2] = 0
            elif rand_int == 1:
                output_F_vector[0] = 0
                output_F_vector[1] = 1
                output_F_vector[2] = 0
        
        
        # -- Set the output vector:
        print("- OUTPUTS:")
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
        sleep(sleep_time)
        
        # - CLOCK 1:
        # -- Set the clock to 1:
        GPIO.output(7,GPIO.HIGH)
        sleep(0.005) # 5ms delay: arduino takes 1ms for each output!
        
        # -- Measire the inputs:
        input_F_vector[0] = GPIO.input(36)
        input_F_vector[1] = GPIO.input(38)
        input_F_vector[2] = GPIO.input(40)
        print("INPUTS:")
        print(input_F_vector)
        
        
        # - Decide the reward type:
        # -- Trivial test:
        if test_type == 1:
            if input_F_vector == [1,0,0]:
                reward = 100
            else:
                reward = 0
                
        # -- Simple test:
        if test_type == 2:
            if rand_int == 0:
                if input_F_vector[0] == 0 and input_F_vector[1] == 1 and input_F_vector[2] == 0:
                    reward = 100
                else:  
                    reward = 0
            elif rand_int == 1:
                if input_F_vector[0] == 1 and input_F_vector[1] == 0 and input_F_vector[2] == 0:
                    reward = 100
                else:  
                    reward = 0
        
        
        # - Provide the reward (0 < r < 100):
        print("REWARD")
        if reward == 100:
            my_pwm_negative.start(0)
            my_pwm_positive.start(100)
            print("- POSITIVE (+) REWARD")
        else:
            my_pwm_negative.start(100)
            my_pwm_positive.start(0)
            print("- NEGATIVE (-) REWARD")

        
        sleep(sleep_time)
        
        # - Stop reward:
        my_pwm_negative.start(0)
        my_pwm_positive.start(0)
  
except:
    print(" ")
    print("Cleaning GPIO and exiting...")
    GPIO.cleanup()
    print("Done!")
