# Research Description:
#### The problem:
- Neural Networks (NNs) and Conventional Computers (CCs) are separate types of Input/Output Machines, but yet every NN only successfully exists as a simulation in a CC.
- Most of the research today is concentrated on optimizing NNs to be a better fit for CCs, or making CCs a better host for NNs.

#### The motivation:
- I believe that we need to start building stand-alone NNs, if we want to achieve the success of CCs.
- If we design the NN in a "smart" way, that will no longer require our CCs to carry out the heavy tast of optimizing, but as to outsource that job to the laws of nature, we can start redirecting our effort from building ligther optimization algorithms to scaling the NNs. Making smaller neurons, making faster connections - those are the actions that will start the exponential increase of power of the NNs and initiate the new Moore's Law, this time for cells in the NNs.

#### The conjecture:
- The main obstruction is the Global nature of the current successful optimization (learning) algorithms. We state the optimization problem as a system of linear equations to make it easier for the CC to compute and then compromise and polish out edges.
- But in general, to update a weight, one needs to ask the CC to carry out optimization task, "minding" the relation of that one weight with respect to all others. And then the CC needs to do this for all weights to complete one step.
- If the Global nature of the process is the obstruction, then the solution would be to make a Local process, Local rules that every part of the NN will follow and out of which the Learning, Optimization and Intellect will be able naturally emerge.

#### The Confusion Point:
- It is one of the most important objects of my study, so I'll make a formal definition of it here.
- <b>Definition:</b> When scaling an NN, which uses a Local learning algorithm, the predictive power (P) of the NN would start increasing with the increase of the NN's scale/complexity (C).The confusion point is the point of C at which P drops. Or:
    - dP/dC > 0 up to the Confusion point for a given Local learning algorithm
- When the goal is natural emergence, there is no way around dealing with chaotic behaviour.

<br><br>
# Reseach Progress:
### The Static Covariant Feedback System</b>:
- The Static Covariant Feedback System is an ANN-like Logistic Regression System.
- It uses a Local "covariant" learning algorithm that independently updates weights between the cells:
- - At cell scale, every neuron records what reward it's receiving given the state of the every other neuron connected to it (Record R(A|B)
- - Then affects P(B) by modifying the weight that connects them W(AB)
- This way, even without hidden layers, the NN learns to pass all Naive classification tasks. When hidden layers are added Confusion doesn't occur.
- The NN fails to learn more complex classification tasks without additional hidden layers (tasks, like when the answer depends not only on the separate inputs, but on specific combinations of them)
- When adding a hidden layer for the complex classification, cofusion would occur. Adding special connections that allow neurons to supress predecessor neurons when needed, fixes this problem. Currently experimenting on the nature of those connections.
- Further helping against confusion come additional memory feature of the neuron connections. They keep track of how their source and target neurons co-vary, to supress unnesessary weigh modifications. This was the original concept, hence I named the network "Covariant Feedback System", butam now polishing few edges to be able to fully implement this idea.
- Further helping against confusion are risk tracking calculations, since every weight modification helps confusion arrise, it's not worth doing a big change on a weight to reduce the change the P(B) if the reward difference on A given B active/notAvtive is not that great.


### The Predictor System:
- The Predictor System is a CNN-like Continuous Regression System.
- It takes "timestamps" of continuous data, like stock prices, and predicts the values for the next N timestamps (future prices).
- The learning algorithm is Local, similar to the one used in the Static Covariant Feedback System, but the Cell-to-Cell connections are static (constant weights), and instead every cell uses covariant connection to the newest input.
- Every cell then makes independent prediction, and the final prediction is a weighted sum of the cell predictions, with the weights beeing the Ratings that each cell has. Then the system simulates itself, using the newest prediction as input, to predict the next future value and repeats this process for N times in order to give N future predictions. Once the new, real value comes, every cell check the prediction it made to update its own Rating.
- Right now it dedicates a whole input array as memory for one input variable, and uses the hidden layers as just combination trackers of that variable, but the main focus is outsorsing the memory job to the hidden layers as well - once the hidden layers are able to act as memory of previous events and also serve as a good input mixing device, the network will be able to work with multiple inputs while keeping correct predictions for all of them.
- A minor problem with the Predictor right now are prediction spikes for more complex input generators, where the network prediction would spike (for example, temporary predict stock price of 1000 when the prices normally would vary between 100 and 200), yet this is not a fundamental problem, that needs revisiting the concept, but only needs some polishing (like excluding prediction when divisor is small, averaging out over different predictions, normal outlier supressing business).


## 01.May.2019 - Confusion point avoided!
- Further optimizing the learning algorithm, exporting part of the memory to the connections and running full connections have done it! Confusion point has been avoided and now scaling the NN improves the results as needed!
- Test results: https://github.com/TraxData313/TCRS_NeuralNet_Project/blob/master/ConfAvoidedFirstProve.PNG
