# The simulation problem:
- Neural Networks (NN) (like our brains) and Conventional Computers (CC) are two types of Input Output Machines (IOM);
- Every IOM has n information holders (bits) and 2^n relations between them.
- Whenever you try to simulate one IOM in another, you have to simulate not only the n bits, but also (compute) all the 2^n connections.
- Therefore if the IOM needed t ~ n time to provide output given the input, it will need ~2^t time to ptovide output when simulated in another IOM.
- Here lies the simulation problem of Neural Networks insite Conventional Computers:
- Concept picture: https://raw.githubusercontent.com/TraxData313/TCRS_NeuralNet_Project/master/NNinsideCC.bmp


# The Neural Network (NN) inside Conventional Computer (CC) Problem:
- NN would need t ~ n time to compute output given input
- When simulated in CC it would need t ~ 2^n time to compute the same output given the same input
- - One can come up with "naive" algorithms that neglect some of the connection which decreases the computation time
- - For example, in most NNs not every cell is connected to every other cell, but they have only layer to layer connections, but again, if the layers have size n, the connections (weights) between two layers are normally n^2.
- Our computers need to simulate, compute and optimize weights between the neural layers

# Research:
- The goal of this research here it to create a NN design that can run and learn on its own hardware.
