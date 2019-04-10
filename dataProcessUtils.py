# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def importData(fileName): 
	# !!! not tested yet, len(dataset) or len(dataset)-1
	# - Importing the dataset, where label is the last col:
	# NOTE: make sure the data file is in the same folder or modify the script if not!
	dataset = pd.read_csv(fileName)
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, len(dataset)].values
	return X, y
	

def oneHotEncode(X,categoricalDataPosition, avoidDummyTrap=1):
	c_d_p = categoricalDataPosition
	# - Encoding categorical data
	from sklearn.preprocessing import LabelEncoder, OneHotEncoder
	labelencoder = LabelEncoder()
	X[:, c_d_p] = labelencoder.fit_transform(X[:, c_d_p])
	onehotencoder = OneHotEncoder(categorical_features = [c_d_p])
	X = onehotencoder.fit_transform(X).toarray()
	# - Avoiding the dummy variable trap:
	if avoidDummyTrap == 1:
		X = X[:, 1:]
	return X
	
	
def featureScale(X_train, X_test, y_train):
	from sklearn.preprocessing import StandardScaler
	sc_X = StandardScaler()
	X_train = sc_X.fit_transform(X_train)
	X_test = sc_X.transform(X_test)
	sc_y = StandardScaler()
	y_train = sc_y.fit_transform(y_train)
	return X_train, X_test, y_train
	
	
def splitTrainTest(X, y):
	# - Splitting the dataset into the Training set and Test set
	from sklearn.cross_validation import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	return X_train, X_test, y_train, y_test