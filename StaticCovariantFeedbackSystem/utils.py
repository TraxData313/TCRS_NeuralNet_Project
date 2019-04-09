    
# - Normalize input data (stdiv):
def normalizeStd(array):
	return (array - array.mean()) / array.std()
    
# - Normalize input data (min-max):
def normalizeMinMax(array):
	return (array - array.mean()) / (max(array) - min(array))




# - Bound input (min < input < max):
def boundInputMinMax(input, min_value, max_value):
    if input < min_value:
        input = min_value
    elif input > max_value:
        input = max_value
    return input
   
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
    return ((old_value*resistance)+new_value)/float(resistance+1)
    


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
