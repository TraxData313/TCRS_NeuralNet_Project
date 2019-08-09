### The General Classifier:
- The General Classifier is a Reaction (Logistic Regression) System
- The system can be interfaced with Convolution layers or any other special layers to perform any task a general ANN would perform
- This is “ready to go” system, that achieves the success of Deep Networks, while ready to implement in stand-alone HW
- It takes N inputs, passes the IO through D hidden layers and provides output out of M possible classes
- Every cell either fires or not, even if the network suppresses specific cell from firing it still has a chance to fire. Similar to dropout mechanism, that prevents network depending only on a few cells, naturally avoiding overfitting and ensures robustness 
- Special relation tracking to weight updating rules are applied, such to minimize unnecessary weight updates, avoiding the Confusion point with scaling of the system
- To do basic tests on the network run tester.py from the same folder as the networkMod.py and utils.py modules
- There are also two more tests included: wine_test.py (on wine.data) and churn_test.py (on Churn_Modelling.csv)
- The General_Classifier_test.ipynb contains the churn_test.py and compares it with the keras ANN Adam done in Jupyter Notebook format

<br>

### The_Alpha_version:
- The folder contains the first Local Learning algorithm, reviews and tests.

<br> 

### The_HW_implementation:
- The folder contains the Arduino based Artificial Brain project information and code
- Documentation vodeos: https://www.youtube.com/watch?v=nxF3fHxuEEI&list=PLNsnBmVpuum4HeMlcsKfv-_SqI4RB8jL9
