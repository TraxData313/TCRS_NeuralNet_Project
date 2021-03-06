## NOTE:
- I will upload the HW implementation progress here, and generally won't be typo hunting, checking it there is missing context or rewriting text to make it preatty. 
- If somebody else is tracking this log - please have that in mind. If something is confisung, please do not hesitate to contact me.

<br>
<hr>
<br>

## Progress:
#### Pre-testing:
- Once I received the first 2 Arduino Nanos, I've uploaded the full code to them, but ran into constant signal transmitting problems (clock not reading ok all the time, not all outputs reading but just one...). 
- Initially the SRAM got filled at about 90% and the arduino would stop functiong normally, but reducing dependent variables helped brind that below 80% and this problem got fixed. Now one arduino nano can house 3 cells with 12 inputs (4 inputs/cell), with total of 36 connections.
- But overall the learning algorithm worked. 
- I've uploaded two "pre-testing" videos:
- - https://www.youtube.com/watch?v=nxF3fHxuEEI&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=1
- - https://www.youtube.com/watch?v=qMZxi_VgzKk&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=2
- If not the few IO bugs, the system proves very stable as expected. Specific inputs can fail, but even with a few still working, the system leanrs.
- The inputs can be physically removed and switch with one another without powering off to recable, and the system re-learns, adapts to the new situation.

<br>

#### Update:
- Today I'm starting to methodically build the first neuron patch, slowly adding feature by feature, testing it extensively to make reduce possible bugs as much as possible
- Created the initial test board with two Arduino Nanos
- One nano is meanth to be the clock and the other is a neuron patch
- Each nano has 3 inputs and 3 outputs initially
- Test1 - 11_IOtest.txt: made sure the IO connections are working alright
- Test2 - 12_ClockSync.txt: made sure the neuron patch follows the bool clock signal
- - video: https://www.youtube.com/watch?v=-4kGPE0uygs&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=3

<br>

#### Update:
- Code used: 13_IOandClock.txt
- Progress halted again by the signal transmititng problem - can't get all 7 signals to transmit properly from the clock to the neuron patch arduino without disturbance;
- - 7 signals: I'm right now trying to get signal going ok between 3 inputs, 3 outputs and a clock per arduino
- If I use that old breadboard I have, the signal would fail somewhere on the breadboard... I keep patching it with additional wires when I find somewhere the signal failing, but I gave up on that yesterday
- Today I tried attaching the two arduinos directly - failed to get all signals going ok, but, of course, the input pins are not pulled down, and the possibility of the issue comming from interfierence is preventing me from any troubleshooting
- - Signal interference problem video: https://www.youtube.com/watch?v=Xoc0MXqBUcI&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=4
- I have one more half-size breadboard which works fine, but I can't get the two arduinos on it.
- At this point I have to wait for additional parts to arrive. They will most likely start arriving in June
- Waiting for some about 15 more arduino nanos, some 20 half-size breadboards, jumperwires and resistors. Orders are distributed in patches from different selles.

<br>

#### Update:
- Started testing Raspberry PI as the clock and Arduino Nano as a neuron patch:
- Test1 - Clock Sync:
- - Clock: piclock12_ClockSync.py
- - Patch: patch12_ClockSync.txt
- - Setup Raspberry Pi. Tested passing the clock signal from the Pi to the Arduino - test passed.
- - Video: https://www.youtube.com/watch?v=XbsuLQ8ncGA&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=5
- Test2 - IO between wires:
- - Clock: piclock11_IOtest.py
- - Patch: patch11_IOtest.txt
- - IO is working with no disturbances. Raspberry build in pull down resistors are very useful. Test passed.
- Test3 - IO and Clock:
- - Clock: piclock13_IOandClock.py
- - Patch: patct13_IOandClock.txt
- - The devices sync with the clock bus. 
- - On low clock Pi provides 3 outputs and Nano reads them. 
- - On high clock Nano provides 3 outputs (output = input) and Pi reads them.
- - For now no signal interuptions or interfierence detected. I'll be able to start testing the learning algorithm now, hopefully without any more electric IO problems. (CORRECTION: need to test transmitting the rewards as well!)
- - Video: https://www.youtube.com/watch?v=TR9WXc85d60&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=6

<br>

#### Update:
- The reward needs to be int (not bool), but Raspberry doesn't have analog outputs. Instead I can turn the pin on and off with specific Hz using GPIO.PWM(pin,Hz)
- When don't analog read from the Arduino on that output from the Pi, it would get high or low. To fix that, I do 1k measurments and take the average
- The reading on the arduino is between 33 and 707 -> reading = (reading - 33)/700 or just reading = reading/700 to get it in range somewhat between 0 and 1
- Now having the (-) and (+) reward busses, the final reward = reward_positive - reward_negative, -1 < reward < 1
- Code used:
- - patch14_rewards.txt
- - piclock14_rewards.py
- - Video: https://www.youtube.com/watch?v=JzKRxfuoABw&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=7

<br>

#### Update:
- Inventory log:
- - 25 half-size breadboards arrived
- - Pic: breadboards_21.May.2019.JPG

<br>

#### Update:
- Full Clock, Reward and IO test
- Raspberry sends output, Arduino reads, copies it and sends it back, Raspberry compares the input with the original output and if correct gives positive reward, else gives negative reward. Both devices sync on the clock signal.
- Code used:
- - patch15_ClockRewardIO.txt
- - piclock15_ClockRewardIO.py

<br>

#### Update:
- Uploaded the learning algorithm on the nano and tested with the trivial test - passes, weights learning is as expected
- <b>Trivial test</b>: passing constant input to the neuron patch, and the expected answer (output) is also constant
- NOTE: Blue LED on the arduino is programed to be on when recieving positive reward
- Video: https://www.youtube.com/watch?v=_1S2kqyMNh4&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=9
- <b>Simple test</b>: answer depents on output - also passes this test
- - If output=[1,0,0], answer=[0,1,0]
- - If output=[0,1,0], answer=[1,0,0]
- - Sample weight convergence: 

0.0 0.0 0.0  
-0.47 -0.74 1.14  
-0.84 1.02 -1.20 
- NOTE: When the cloch Hz get lower, the analog outputs start failing (when sleep_time param < 0.3)
- Used code:
- - piclock17_trivialAndSimpleTests.py
- - patch16_working3v3.txt


<br>

#### Update:
- Finished the extended learning algorithm

<br>

#### Update:
- All parts have already arrived (arduinos, cables, resistors...)
- Only thing left is the power supply. Looking for suitable power supply...

