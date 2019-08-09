import numpy as np
import random
import time
import utils
import matplotlib.pyplot as plt
from networkMod import Network
import matplotlib.patches as mpatches
from utils import println
import pandas as pd
from sklearn.metrics import confusion_matrix


# PART 1 - GETTING THE DATA READY:
println(5)
print("Getting the data ready...")

# Importing the dataset
dataset = pd.read_csv('wine.data')
X = dataset.iloc[:, 1:14].values
y = dataset.iloc[:, 0].values

'''
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
# - Taka care of the dummy variable trap:
X = X[:, 1:]
'''


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)





print()
print("Done!")



# PART 2 - GETTING THE NEURAL NETWORK READY:
println(5)

# - Setting the parameters:
input_size   = len(X_test[0])
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




# PART 3 - TRAINING THE NEURAL NETWORK:
# - Prepare the grapth data:
learning_rate = [[],[]]

println(5)
print("NOTE that the Demo Classifier is a fast learner!")
print()
epochs = input("Choose the epochs of training: ")
epochs = int(epochs)

# - Set the max learning of the network:
max_learn = len(X_train)*epochs/2
sampleNetwork.max_EF_resist = max_learn
sampleNetwork.D_resist      = max_learn

for epoch_numb in range(epochs):
    y_pred = []
    score_list = []
    for test_numb in range(len(X_train)):
        # - Get input:
        X_train[test_numb]
        input_ = X_train[test_numb]
        
        # - Input to the neural net:
        sampleNetwork.getInputAndPropagate(input_)
        
        # - Get the output:
        output = sampleNetwork.returnOutputPlace()
        y_pred.append(output)
        
        # - Compare with the y_train output:

        if y_train[test_numb] == output+1:
            feedback =  0.5
        else:
            feedback = -0.5
        
        # - Feedback:
        sampleNetwork.rewardAndUpdate(feedback)
        
        # - Calculate score (% of right answers):
        if feedback > 0:
            new_score = 1
        else:
            new_score = 0
            
        score_list.append(new_score)
        
        # - Every Nth turn:
        Nth_turn = 10
        if test_numb % Nth_turn == 0 and test_numb != 0 and test_numb != Nth_turn:
                
            correctness = np.mean(score_list)
        
            # - Append the learning rate list:
            learning_rate[0].append(correctness)
            try:
                learning_rate[1].append(np.mean(learning_rate[1][-1]+Nth_turn))
            except:
                learning_rate[1].append(0)
                
            # - Print data:
            print()
            print("Inner weights:")
            sampleNetwork.printLLClist()
            print()
            print("Outer weights:")
            sampleNetwork.printLOClist()
            println(5)
            print()
            print("Epoch  :", epoch_numb)
            print("Test   :", test_numb)
            print("Correctness %:", correctness*100)

    
# PART 4 - PREDICT THE TEST SET:
y_pred = []
score_list = []
println(5)
print("Evaluating on the test set...")
for test_numb in range(len(X_test)):
    # - Get input:
    X_test[test_numb]
    input_ = X_test[test_numb]
    
    # - Input to the neural net:
    sampleNetwork.getInputAndPropagate(input_)
    
    # - Get the output:
    output = sampleNetwork.returnOutputPlace()
    y_pred.append(output)
    
    # - Compare with the y_train output:
    if y_test[test_numb] == output+1:
        feedback = 0.5
    else:
        feedback = -0.5
    
    # - Continue learning through the test set?:
    #sampleNetwork.rewardAndUpdate(feedback)
    
    # - Calculate score (% of right answers):
    if feedback == 0.5:
        new_score = 1
    else:
        new_score = 0
    score_list.append(new_score)
    
    # - print every 100 turns:
    if test_numb % 10 == 0:
        print(test_numb)
       
        
# Result:
print("Done!")
println(3)
print("Tested network:")
print(sampleNetwork)
print("- For", epochs, "epochs")
print()
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(cm)
print()
print("Correct answers in %:", np.mean(score_list)*100)
print()
print(score_list)
print()

'''
# - View the data:
view_data = input("Do you want to view the data (1 or 0)? ")
view_data = int(view_data)
if view_data == 1:
    # Plot the data:
    plt.scatter(learning_rate[1], learning_rate[0], s=100, alpha=0.5)
    # c = Y, pick a color for every Y
    plt.show()
'''

view_data = input("Do you want to view learning curve? (1 or 0) ")
view_data = int(view_data)
if view_data == 1:
    plt.xlabel('Training sample')
    plt.ylabel('Correctness')
    plt.plot(learning_rate[1], learning_rate[0], color="green")
    green_line = mpatches.Patch(color='green', label='Total Error')
    plt.legend(handles=[green_line])
    plt.show()