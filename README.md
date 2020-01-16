## The problem:
- Neural Networks (NNs) and Conventional Computers (CCs) are separate types of Input/Output Machines, but NNs only successfully exists as a simulation in a CC.
- Most of the research today is concentrated on optimizing NNs to be a better fit for CCs, or making CCs a better host for NNs.

## The Research Goal:
- Build a stand-alone, scalable NN from self-similar elements (cells and weights circuits), such that increasing the number of elements in the network will proportionally increase its power, but keeping the learning time unchanged.
- Achieving this will initiate the new Moore's Law, this time of NNs.

## The obstruction:
- Current learning and optimization algorithms are Global.
- Changing a single weight , influences the IO passing through every other successor weight.
- If we build a self-optimizing weight, which learns based on this Global mechanism, in general, every weight will have to be connected to every other weight.
- Network of N weights will need to have 2^N connections between the weights.
- So now if we start scaling the NN, with every new weight, every weight will have to compute increasingly more complex equation, having to track how it affects all the other weights to change itself every time, making the learning time exponential with the network size.

## The possible solution:
- Self-similar cells and self-similar weights, following the same (Local) rules, every weight keeping track only of the states of the two cells it is connecting, to compute how to change itself, in such a way, that out of the cumulative effect of all connections changing, the Intellect of the system will emerge, and with the increase of the size of the system, the Intelect will increase.
- Normally when scaling an NN, which uses a Local learning algorithm, the prediction error (E) of the NN would start decreasing with the increase of the NN's scale/complexity (C). The confusion point is the point of C at which the NN loses that behaviour. Or:
- - dE/dC < 0 up to the Confusion point for a given Local learning algorithm. After that dE/dC >= 0

## Research Progress:
- In my research I’ve been able to find a set of Local learning rules and connection topologies, that allow the scaling of the Network, decreasing the prediction error, while avoiding the Confusion point
- Based on that I’ve been able to build two types of Neural Networks, The General Classifier and The Predictor
- Currently I'm researching "lighter", working topologies for the General Classifier and I've also started the process of finding the first "Host" HW to start building an artificial brain. I'll be logging my progress in the "<b>implementing the general classifier</b>" folder.
- Also currently researching a way to massively expanding the input space of every cell by encoding information into permutations of the input. Right now looking for the possible distance metrics and how the method with which the cell "chooses" one in order to maximixe usefullness.
- - NOTE: Done. Initial results and control test in the Simple Permutator folder. Further development in separate repo: Permutator.

<br>
<br>
<hr>
<br>
<br>

## The General Classifier:
- The General Classifier is a Reaction (Logistic Regression) System
- The system can be interfaced with Convolution layers or any other special layers to perform any task a general ANN would perform
- This is “ready to go” system, that achieves the success of Deep Networks, while ready to implement in stand-alone HW
- It takes N inputs, passes the IO through D hidden layers and provides output out of M possible classes
- Every cell either fires or not, even if the network suppresses specific cell from firing it still has a chance to fire. Similar to dropout mechanism, that prevents network depending only on a few cells, naturally avoiding overfitting and ensures robustness 
- Special relation tracking to weight updating rules are applied, such to minimize unnecessary weight updates, avoiding the Confusion point with scaling of the system
- Code, tests, Jupyter notebook review and the HW implementation projects with Arduino Nano are in the <b>"GeneralClassifier"</b> folder

## Simple Permutator:
- The natural weight system, developed under this project, the Permutator networks became possible.
- Given input of size N, the Permutator cell takes every permutation of the input as a separate signal.

## The Predictor:
- The Predictor is a continuous data Regression System
- The predictor is still a prototype system, and in active research. It’s “future-predictive” power combined with the “reaction” and learning power of the General Classifier, is meant to make an independent, local rule-based Reinforcement Learning Platform
- The Predictor takes “timestamps” of continuous data and predicts the next one
- Once the next prediction is made, the Predictor simulates itself with the new prediction as the new input to predict the yet next input
- This process is repeated for N times, depending how “long” of a prediction is needed
- Micro and Macro-based Rating systems make sure that the best prediction is made and that every prediction “timestamp” has a proper accuracy probability to it
