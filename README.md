# Research Description:
#### The problem:
- Neural Networks (NNs) and Conventional Computers (CCs) are separate types of Input/Output Machines, but yet every NN only successfully exists as a simulation in a CC.
- Most of the research today is concentrated at optimizing the NNs to be a better fit for the CCs, or making the CCs a better host for the NNs.

#### The motivation:
- I believe that we need to "free" the NNs, if we want to achieve the success of the CCs.
- If we build the NNs in a "smart" way that will no longer need our CCs to carry out the heavy tast of optimizing them, but as to outsource that job to the laws of nature, we can stop finding ways to build ligther optimization tasks, but start working on making smaller neurons, making faster connections... Start the process of scaling the number of neurons in the networks as fast as how we were/are scaling the number of transistors in our computers, achieve the Moore's Law of NNs.

#### The conjecture:
- The main obstruction is the Global nature of the current successful optimization (learning) algorithms. We state the optimization problem as a system of linear equations to make it easier for the CC and then compromise and polish out edges.
- But in general, to optimize a weight, one needs to ask the CC to compute a function, having in mind the relation of that one weight with respect to all others. And then the CC needs to do this for all weights.
- If the Global nature of the process is the obstruction, the solution would be to make a Local process, Local rules that every part of the NN will follow and of which the Learning, Optimization and Intellect will be able naturally emerge.

#### Research notes:
- This is what this research is about, and in the section below I'll be tracking its progress.
- Why I work on this? I think we'll need the best symmetry extractor if we are to start braking the problem of extracting all the symmetrys in nature.
- One important them I will use the <b>the Confusion point</b>, so I'll loosely define it here as the point complication for a given learning algorithm at which the system stops learning when given its rewards, but instead converges to chaotic behaviour.


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
