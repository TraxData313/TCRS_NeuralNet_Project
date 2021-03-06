import numpy as np
import random
import time


# - Standardize input data (-1<x<1):
def normalizeStd(array):
	return (array - array.mean()) / array.std()
    
# - Normalize input data (0<x<1):
def normalizeMinMax(array):
	return (array - array.mean()) / (max(array) - min(array))
'''
# using sklearn:
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)
'''



# - Bound input (min < input < max):
def boundInputMinMax(input, min_value, max_value):
    if input < min_value:
        input = min_value
    elif input > max_value:
        input = max_value
    return input
    
# - Bound input array (min < input < max):
def boundInputMinMaxArray(array, min_value, max_value):
    for n in range(len(array)):
        if array[n] < min_value:
            array[n] = min_value
        elif array[n] > max_value:
            array[n] = max_value
        return array


   
# - Bound input (min < input):
def boundInputMin(input, min_value):
    if input < min_value:
        input = min_value
    return input


# - Standardize sigmoid:
def sigmoid(input):
	return 1/(1 + np.exp(-input))
    

    
# - Standard covarriance of X1 and X2:
def COV(X1,EX1,X2,EX2):
    COV = (X1-EX1)*(X2-EX2)
    return COV
    
    
# - Moving average:
def movingAverage(old_value, new_value, resistance):
    result = (old_value*resistance+new_value)/(resistance+1)
    return result
    


# - takes predicted and real binary labes and gives prediction correctness:
def classification_rate(Y, P):
	return np.mean(Y == P)



'''
Cross-Entropy Error (cost) function
J = - SUM{ ( t*log(y) + (1-t)*log(1-y) ) } , where t = target, y = output of logistic
ex:
t = 1, y = 1 -> J = 0
t = 0, y = 0 -> J = 0
t = 1, y = 0,9 -> 0,11
t = 1, y = 0,1 -> 2,3
'''
# calculate the cross-entropy error
def cross_entropy(T, Y):
    E = 0
    for i in range(len(T)):
        if T[i] == 1:
            E -= np.log(Y[i])
        else:
            E -= np.log(1 - Y[i])
    return E

    
def println(lines):
    for n in range(lines):
        print(" ")
        
        
        
# - Create diagnolized matrix:
def diagonalized(rows, cols, min=-1, max=1):
    temp_matrix = np.zeros((rows, cols))
    for row in range(rows):
        for el in range(cols):
            if el == row or el-1 == row or el+1 == row:
                temp_matrix[row][el] = random.randint(min*100,max*100)/100.
    return temp_matrix
#


def runConnectionsPush(array_matrix, conn_matr_list, norm=0):
    # A[n+1] = np.dot(A[n],M[n])
    for n in range(len(array_matrix)-1):
        array_matrix[n+1] = np.dot(array_matrix[n],conn_matr_list[n])
    return array_matrix
    
def runConnectionsPull(array_matrix, conn_matr_list, norm=0):
    # A[n+1] = np.dot(A[n],M[n])
    n = len(array_matrix)-2
    while n >= 0:
        array_matrix[n+1] = np.dot(array_matrix[n],conn_matr_list[n])
        n = n - 1
    return array_matrix





















