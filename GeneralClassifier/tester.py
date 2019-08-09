import numpy as np
import random
import time
import utils
import matplotlib.pyplot as plt
from networkMod import Network
from utils import println
import pandas as pd



println(10)
print("Test variants:")
print(" - 0 for Simple test  : Constant Answer")
print(" - 1 for Basic test   : Dependent Answer")
print(" - 2 for Classifier   : Answer(Coordinate)")
print(" - 3 for Permutation  : Answer(Perm(input))")
testVariant = input("Please choose a test: ")
testVariant = int(testVariant)



#########################
# SIMPLE AND BASIC TESTS:
if testVariant == 0 or testVariant == 1:
    print()
    if testVariant == 0:
        print(" - Simple test: Constant Answer")
        print("   Input may be [0,1] or [1,0]")
        print("   Correct answer is always [0,1]")
    elif testVariant == 1:
        print(" - Basic test: Varying Answer")
        print("   if input=[0,1], asnwer=[0,1]")
        print("   if input=[1,0], asnwer=[1,0]")
    # - Parameters:
    input_size   = 2
    print()
    hidden_count = input("Please specify hidden network count: ")
    hidden_count = int(hidden_count)
    if hidden_count == 0:
        hidden_size = 0
    else:
        print()
        hidden_size  = input("Please specify hidden network size: ")
        hidden_size  = int(hidden_size)
    output_size = 2
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
            
        # - getInputAndPropagate:
        sampleNetwork.getInputAndPropagate(input)
        
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
        sampleNetwork.rewardAndUpdate(feedback/2.)
        
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
            sampleNetwork.printLLClist()
            print()
            print("Outer weights:")
            sampleNetwork.printLOClist()
            println(5)
            print("Tick:", tick)
            print(sampleNetwork)
            print("Output  :", output)
            print("Feedback:", feedback)
            print("Correct in %:", correctness)
            time.sleep(0.5)
        tick += 1
# END SIMPLE AND BASIC TESTS
############################



##################
# CLASSIFIER TEST:
elif testVariant == 2:
    print()
    print(" - Classifier: Answer as a function of position")
    print("   Generate 3 clusters of point on 2D grid")
    print("   Pass X1 and X2 coordinates as input")
    print("   Machine learns to classify which dot came from where")
    print()

    # - Create the data:
    D = 2 # dimensionality of the input
    Nclass = 500
    '''
    X1 = np.random.randn(Nclass, D)/5. + np.array([0.7 ,0]) #center on x=0, y=-2
    X2 = np.random.randn(Nclass, D)/5. + np.array([0.7 , 0.7])
    X3 = np.random.randn(Nclass, D)/5. + np.array([0, 0.7])
    '''
    X1 = np.random.randn(Nclass, D) + np.array([0 ,-2]) #center on x=0, y=-2
    X2 = np.random.randn(Nclass, D) + np.array([2 , 2])
    X3 = np.random.randn(Nclass, D) + np.array([-2, 2])
    
    X  = np.vstack([X1,X2,X3])
    Y = np.array([0]*Nclass + [1]*Nclass + [2]*Nclass)
    
    # - View the data:
    view_data = input("Do you want to view the data (1 or 0)? ")
    view_data = int(view_data)
    if view_data == 1:
        # Plot the data:
        plt.scatter(X[:,0], X[:,1], c=Y, s=100, alpha=0.5)
        # c = Y, pick a color for every Y
        plt.show()

    # - Parameters:
    input_size   = 2
    print()
    hidden_count = input("Please specify hidden network count: ")
    hidden_count = int(hidden_count)
    if hidden_count == 0:
        hidden_size = 0
    else:
        print()
        hidden_size  = input("Please specify hidden network size: ")
        hidden_size  = int(hidden_size)
    output_size  = 3
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
        rand_class = random.randint(0,2)
        if rand_class == 0:
            rand_sample = random.randint(0,Nclass-1)
            sample = X1[rand_sample]
        elif rand_class == 1:
            rand_sample = random.randint(0,Nclass-1)
            sample = X2[rand_sample]
        elif rand_class == 2:
            rand_sample = random.randint(0,Nclass-1)
            sample = X3[rand_sample]

        # - getInputAndPropagate:
        sampleNetwork.getInputAndPropagate(sample)
        
        # - Get the output:
        output = sampleNetwork.returnOutputPlace()

        # - Check if the output is correct and return the feedback:
        if rand_class == 0:
            if output == 0:
                feedback = 1
            else:
                feedback = - 1
                
        elif rand_class == 1:
            if output == 1:
                feedback = 1
            else:
                feedback = - 1
                
        elif rand_class == 2:
            if output == 2:
                feedback = 1
            else:
                feedback = - 1
        
        # - feedback the network:
        sampleNetwork.rewardAndUpdate(feedback/2.)
        
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
            sampleNetwork.printLLClist()
            print()
            print("Outer weights:")
            sampleNetwork.printLOClist()
            println(5)
            print("Tick:", tick)
            print(sampleNetwork)
            print("Output  :", output)
            print("Feedback:", feedback)
            print("Correct in %:", correctness)
            time.sleep(0.5)
        tick += 1
# END CLASSIFIER TEST
#####################



####################
# PERMUTATIONS TEST:
elif testVariant == 3:
    print()
    print(" - Simple Permutation Test: Anser(Perm(Input))")
    print("   If input=[1,0], answer=[1,0,0]")
    print("   If input=[0,1], answer=[0,1,0]")
    print("   If input=[1,1], answer=[0,0,1]")
    print("   Test if the machine's hidden layers can")
    print("   learn from the connections in the input")
    print()
    # - Parameters:
    input_size   = 2
    print()
    hidden_count = input("Please specify hidden network count: ")
    hidden_count = int(hidden_count)
    if hidden_count == 0:
        hidden_size = 0
    else:
        print()
        hidden_size  = input("Please specify hidden network size: ")
        hidden_size  = int(hidden_size)
    output_size = 3
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
        someInt = random.randint(0,2)
        if someInt == 0:
            input.append(1)
            input.append(0)
        elif someInt == 1:
            input.append(0)
            input.append(1)
        else:
            input.append(1)
            input.append(1)
            
        # - getInputAndPropagate:
        sampleNetwork.getInputAndPropagate(input)
        
        # - Get the output:
        output = sampleNetwork.returnOutputPlace()
        
        # - Check the answer:
        if someInt == 0:
            if output == 0:
                feedback = 1
            else:
                feedback = -1
        elif someInt == 1:
            if output == 1:
                feedback = 1
            else:
                feedback = -1
        elif someInt == 2:
            if output == 2:
                feedback = 1
            else:
                feedback = -1
                
        # - feedback the network:
        sampleNetwork.rewardAndUpdate(feedback/2.)
                
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
            sampleNetwork.printLLClist()
            print()
            print("Backward weights:")
            sampleNetwork.printLBClist()
            print()
            print("Outer weights:")
            sampleNetwork.printLOClist()
            println(5)
            print("Tick:", tick)
            print(sampleNetwork)
            print("Output  :", output)
            print("Feedback:", feedback)
            print("Correct in %:", correctness)
            time.sleep(0.3)
        tick += 1
# END PERMUTATIONS TEST
#######################



























