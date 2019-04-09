import numpy as np
import random
import time
import utils
from networkMod import Network
from utils import println


println(10)
testVariant = input("Please choose a test from 0 to 5:")
testVariant = int(testVariant)
if testVariant == 0 or 1:
    print()
    if testVariant == 0:
        print(" - Simple test: Constant Answer")
        print("   Input may be [0,1] or [1,0]")
        print("   Correct answer is always [0,1]")
    elif testVariant == 1:
        print(" - Basic test: Varying Answer")
        print("   if input=[0,1], asnwer=[0,1]")
        print("   if input=[1,0], asnwer=[1,0]")
    print()
    # - Parameters:
    input_size   = 2
    hidden_size  = input("Please specify hidden network size:")
    hidden_size  = int(hidden_size)
    output_size  = 2
    hidden_count = input("Please specify hidden network count:")
    hidden_count = int(hidden_count)
    print()
    print("Creating a network...")
    sampleNetwork = Network(input_size,
                            hidden_size,
                            output_size,
                            hidden_count)
    time.sleep(0.5)
    print("Done!")
    print(sampleNetwork)
    
    score_list = [0]*100
    println(25)
    tick = 0
    while True:
        # - Prepare the input:
        input = []
        someInt = random.randint(0,1)
        if someInt == 0:
            input.append(1)
            input.append(0)
        else:
            input.append(0)
            input.append(1)
            
            
        # - inputAndUpdate:
        sampleNetwork.inputAndUpdate(input)
        
        
        # - Get the output:
        output = sampleNetwork.returnOutputPlace()
            
        # - if Simple answer:
        if testVariant == 0:
            if output == 1:
                feedback = - 1
            else:
                feedback = 1
        
        # - if Varying answer:
        elif testVariant == 1:
            if someInt == 0:
                if output == 1:
                    feedback = - 1
                else:
                    feedback = 1
            else:
                if output == 1:
                    feedback = 1
                else:
                    feedback = - 1

        # - feedback the network:
        sampleNetwork.feedback(feedback)
        
        # - Calculate score (% of right answers):
        if feedback == 1:
            new_score = 1
        else:
            new_score = 0
        score_list.append(new_score)
        score_list.pop(0)
        
        # - End loop:
        if tick % 100 == 0:
            correctness = np.mean(score_list)
            println(10)
            print("Correct vs wrong answers list:")
            print(score_list)
            print()
            print("Inner weights:")
            print(sampleNetwork.LL_matrices_list)
            print()
            print("Outer weights:")
            print(sampleNetwork.LO_matrices_list)
            println(5)
            print("Tick:", tick)
            print(sampleNetwork)
            print("Output  :", output)
            print("Feedback:", feedback)
            print("Correct in %:", correctness)
            #time.sleep(1)
        tick += 1
#
