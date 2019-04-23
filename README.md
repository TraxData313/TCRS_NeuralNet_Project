# Definitions:
- <b>NNs and CCs</b>: Neural Networks (<b>NN</b>) and Conventional Computers (<b>CC</b>) are two different types of Input-Output Machines (<b>IOM</b>).
- <b>Bits and Gates</b>: Both types (NNs and CCs) contain bit holders (memory) and gates (connections). Gates are logical operations that take as input the state of bit holders and output the result state output bits.
- <b>Base Systems</b>: A base system's Gates are physical circuits, build in such a way, that given the input bits the gates are directly executed by natural laws.
- - Example: the Gates in the CCs are build out of transistors. They are build in a "smart" way, such that given the input currents (+ or -), the laws of electrodynamics will provide the desired output (+ or -).
- <b>Simulated Sistems</b>: On the other hand, a simulated system exists as an abstraction inside another (<b>Host</b>) IOM, and the operations in its Gates are calculated by the Host IOM.

# The Simulation Problem of NNs:
- <b>The problem</b>: Neural Networks, as of now, only exist as simulations within Conventional Computers, and we cannot build a Base NN IOM.

# The obstructions:
- <b>Local Operations</b>: In order to build a Base System, we need to represent all operations as small, simple units of computation, then create "smart", self-similar circuits, like the transistors in the CCs, that can carry out those operations. Once we have those Local units, we can start scaling them to build more powerfull IOM.
- <b>Learning is a Global operation</b>: We can easily represent the bit holders and the weights of the the NNs as Local operations, but the problem comes with weight updating (learning) algorithms, like the general Gradient Descent method, which needs to take as input the whole <b>the Global state</b> of the system in order to update a single weight.
- <b>Exponential scaling</b>: If we are to "bute-force" express an NN right now, an in particular its learning mechanism, in Local therms, we will need to create a circuild between every weight in the system. <b>If we add one weight to a system of N weights, we will need to create 2^N Local units</b>. Hence the obstruction to building a Base NN system - the scaling of the Local circuits that it will need to operate.

# Motivation and Solution:
- <b>Better Learning Algorithm</b>: If the goal is to build a Base NN System and the main obstruction is the scaling of the learning algorithms, the solution would be to build a learning algorithm that doesn't scale exponentially with the complexity of the system.
- <b>Motivation</b>: The human brain contains some 10^10 neurons, each having about 10^4 connections, if it was using exponentially scaling learning method, like the ones we use in our NNs, it would have needed to keep track of some 2^10^14 local variables, which, I believe, is imposible. Instead, my main conjecture is that the cells and their connections have evolved a set of local rules for signal computation and connection updating, that on the macro scale give rise to <b>the Intellect as an emergent phenomenon</b>. Those kinds of micro rules are the main goal of my research here.
 
# Accomplished so far:
<b>The Static Covariant Feedback System</b>
<br>
- The Static Covariant Feedback System is an ANN-like Logistic Regression System.
- It uses a Local "covariant" learning algorithm that independently updates weights between the cells (bit holders).
- With no hidden layers, the system can perform Logistic Regression of any N independent inputs, like classifing a point given N coordinates.
- With a few hidden layers, the system can learn to perform harder Classifier tasks, like predicting whether a Bank customer will Churn.
<p></p>
<b>The Predictor System</b>
- The Predictor System is a CNN-like Continuous Regression System.
- It takes "timestamps" of continuous data, like stock prices, and predicts the values for the next N timestamps (future prices).
- The learning algorithm is Local, similar to the one used in the Static Covariant Feedback System, but the Cell-to-Cell connections are static (constant weights), and instead every cell uses covariant connection to the newest input.
- Every cell then makes independent prediction, and the final prediction is a weighted sum of the cell predictions, with the weights beeing the Ratings that each cell has. Then the system simulates itself, using the newest prediction as input, to predict the next future value and repeats this process for N times in order to give N future predictions. Once the new, real value comes, every cell check the prediction it made to update its own Rating.
