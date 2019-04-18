# The simulation problem:
- Neural Networks (NN) and Conventional Computers (CC) are two types of Input Output Machines (IOM);
- Every IOM has n information holders (bits) and relations between them (complexity).
- IOMs are build in such a way, that the laws of physics carry out the flow computations between the bits, given the state of the bits.
- - For example, the transistors (gates) in out CCs are build in such a way, that they will pass electric signals between the bit holders given their states. We build the transistors in a "smart" way, as to "cheat" the laws of electrodynamics to carry out the computations for us.
- Whenever we try to simulate one IOM in another, we have to simulate not only the n bits, but we also have to manually compute all the information flow on the connections between them -> in general on max of 2^n connections.
- Therefore if the IOM needed t ~ n time to provide output given the input, it will need t ~ 2^n time to ptovide output when simulated in another IOM.
- Here lies the simulation problem of Neural Networks insite Conventional Computers:
- Concept picture: https://raw.githubusercontent.com/TraxData313/TCRS_NeuralNet_Project/master/NNinsideCC.bmp


# The Neural Network (NN) inside Conventional Computer (CC) Problem:
- NN would need t ~ n time to compute output given input
- When simulated in CC it would need, in general, t ~ 2^n time to compute the same output given the same input
- Our computers need to simulate, compute the information flow and optimize the weights between the neural layers


# Research:
- Right now we can't build real (not simulated) NN, because we have no way to "cheat" physics to carry out the learning and optimization of the connections.
- So the goal of this research here it to create a "smart" NN design that can "cheat" the laws of physics into carrying out those tasks for us.


# Current Achievments:
- The Static Covariant Feedback System uses special "covariant" bonds between it's cells which can learn and optimize. It can solve:
- - All Naive Classifier Problems : Answer as a function of position, but not on combinations between coordinates
- - Simple General Classifier Problems : Answer depends not only on position, but also on correlations between coordinates
