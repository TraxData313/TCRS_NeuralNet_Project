# Research Description:
#### The problem:
- Neural Networks (NNs) and Conventional Computers (CCs) are separate types of Input/Output Machines, but yet every NN only successfully exists as a simulation in a CC.
- Most of the research today is concentrated on optimizing NNs to be a better fit for CCs, or making CCs a better host for NNs.

### The Goal:
- Build a stand-alone, scalable NN from self-similar elements (cells and weights circuits), such that increasing the number of elements in the network will proportionally increase its power.
- Achieving this will initiate the new Moore's Law, this time of NNs.

### The obstruction:
- Current learning and optimization algorithms are Global.
- Changing a single weight (in the most general case), influences the IO passing through every other weight.
- If we build a self-optimizing weight, which learns based on this Global mechanism, every weight will have to be connected to every other weight.
- Network of N weights will, in general, need to have 2^N connections between the weights.
- So now if we start scaling the NN, with every new weight, every weight will have to compute increasingly more complex equation, having to track how it affects all the other weights to change itself every time.

### The solution:
- Self-similar cells and self-similar weights between them, following the same (Local) rule, every weight keeping track only of the states of the two cells it is connecting, to compute how to change itself, in such a way, that out of the cumulative effect of all connections changing, the Intellect of the system will emerge, and with increase of the size of the system, the Intelect will increase.
- Normally when scaling an NN, which uses a Local learning algorithm, the prediction error (E) of the NN would start decreasing with the increase of the NN's scale/complexity (C).The confusion point is the point of C at which E increases dramatically. Or:
- - dE/dC < 0 up to the Confusion point for a given Local learning algorithm. After that E -> max

### Research Achievements:
- In my research I’ve been able to find a set of Local learning rules and connection topologies, that allow the scaling of the Network, decreasing the prediction error, while avoiding the Confusion point
- Based on that I’ve been able to build two types of Neural Networks, The General Classifier and The Predictor

<br>
<hr>
<br>

### The General Classifier:
- The General Classifier is an ANN-like Logistic Regression System
- The system can be interfaced with Convolution layers or any other special layers to perform any task a general ANN would perform
- This is “ready to go” system, that achieves the success of Deep Networks, while ready to implement in stand-alone HW
- It takes N inputs, passes the IO through D hidden layers and provides output out of M possible classes
- Every cell either fires or not, even if the network suppresses specific cell from firing it still has a chance to fire. Similar to dropout mechanism, that prevents network depending only on a few cells, naturally avoiding overfitting and ensures robustness 
- Special relation tracking to weight updating rules are applied, such to minimize unnecessary weight updates, avoiding the Confusion point with scaling of the system
- To do a Demo of the Classifier, go to the "General Classifier Demo" folder

### The Predictor:
- The Predictor is a CNN-like Continuous Regression System
- The predictor is still a prototype system, and in active research. It’s “future-predictive” power combined with the “reaction” and learning power of the General Classifier, would make the Super-Reinforcement Learning Platform
- The Predictor takes “timestamps” of continuous data and predicts the next one
- Once the next prediction is made, the Predictor simulates itself with the new prediction as the new input to predict the yet next input
- This process is repeated for N times, depending how “long” of a prediction is needed
- Micro and Macro-based Rating systems make sure that the best prediction is made and that every prediction “timestamp” has a proper accuracy probability to it
