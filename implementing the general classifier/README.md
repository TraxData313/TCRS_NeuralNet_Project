## NOTE:
- I will upload the HW implementation progress here, and generally won't be typo hunting, checking it there is missing context or rewriting text to make it preatty. 
- If somebody else is tracking this log - please have that in mind. If something is confisung, please do not hesitate to contact me.

## Overall progress:
- Pre-testing confirms the learnig algorithm working, and the nano having enough memory to handle 3 cells with 36 connections.
- 15.May.2019: Pre-testing done. Clock and neuron patch IO and clock sync tests done
- 17.May.2019: Progress halted. Waiting for parts.

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
- If not the irritating bugs, the system proves very stable as expected. Specific inputs can fail, but even with a few still working, the system leanrs.
- The inputs can be physically removed and switch with one another without powering off to racable, and the system re-learns, adapts to the new situation.

#### 15.May.2019:
- Today I'm starting to methodically build the first neuron patch, slowly adding feature by feature, testing it extensively to make reduce possible bugs as much as possible
- Created the initial test board with two Arduino Nanos
- One nano is meanth to be the clock and the other is a neuron patch
- Each nano has 3 inputs and 3 outputs initially
- Test1 - 11_IOtest.txt: made sure the IO connections are working alright
- Test2 - 12_ClockSync.txt: made sure the neuron patch follows the bool clock signal
- - video: https://www.youtube.com/watch?v=-4kGPE0uygs&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=3

#### 17.May.2019:
- Progress halted again by the signal transmititng problem - can't get all 7 signals to transmit properly from the clock to the neuron patch arduino without disturbance;
- - 7 signals: I'm right now trying to get signal going ok between 3 inputs, 3 outputs and a clock per arduino
- If I use that old breadboard I have, the signal would fail somewhere on the breadboard... I keep patching it with additional wires when I find somewhere the signal failing, but I gave up on that yesterday
- Today I tried attaching the two arduinos directly - failed to get all signals going ok, but, of course, the input pins are not pulled down, and the possibility of the issue comming from interfierence is preventing me from any troubleshooting
- - Signal interference problem video: https://www.youtube.com/watch?v=Xoc0MXqBUcI&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9&index=4
- I have one more smaller breadboard which works fine, but I can't get the two arduinos on it.
- At this point I have to wait for additional parts to arrive. They will most likely start arriving in June
