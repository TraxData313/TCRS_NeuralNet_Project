# Definitions:
- <br>NNs and CCs</br>: Neural Networks (<br>NN</br>) and Conventional Computers (<br>CC</br>) are two different types of Input-Output Machines (<br>IOM</br>).
- <br>Bits and Gates</br>: Both types (NNs and CCs) contain Bit Holders (memory) and Gates (connections). Gates are logical operations that take as input the state of bit holders and output the result state to (other) bits.
- <br>Base Systems</br>: The Base System's Gates are physical circuits, build in such a way, that given the input bits the gate operations are directly executed by the laws of Nature.
- - Example: the Gates in the CCs are build out of transistors. They are build in a "smart" way, such that given the input currents (+ or -), the laws of electrodynamics will provide the desired output (+ or -).
- <br>Simulated Systems</br>: On the other hand, a simulated system exists as an abstraction inside another (<br>Host</br>) IOM, and the operations in its Gates are calculated by the Host IOM.
- - Concept: https://raw.githubusercontent.com/TraxData313/TCRS_NeuralNet_Project/master/NNinsideCC.bmp

# The Simulation Problem of NNs:
- <br>The problem</br>: Neural Networks, as of now, only exist as simulations within Conventional Computers, and we haven't build a real, Base NN IOM.

# The obstruction:
- <br>The need for Local Operations</br>: In order to build a Base System, we need to represent all operations as small, simple units of computation, then create "smart", self-similar circuits, like the transistors in the CCs, that can carry out those operations. Once we have those Local units, we can start scaling them to build more powerfull IOMs.
- <br>Learning is a Global Operation</br>: We can easily represent the bit holders and the weights of the the NNs as Local operations, but the problem comes with the weight updating (learning) algorithms, like the general Gradient Descent method, which needs to take as input the whole <br>Global state</br> of the system in order to update a single weight. So a Global Operation needs (takes as input) the state of every unit to output the state of a single, target unit.
- <br>Exponential scaling</br>: Given the global nature of the learning mechanism, if we are to "brute-force" express an NN right now, in Local therms, we will need to create a circuit between each weight in the system. <br>If we add one weight to a system of N weights, we will need to create 2^N Local units</br>. Hence the obstruction to building a Base NN system - the scaling of the Local circuits that it will need to operate.

# The solution:
- <br>Better Learning Algorithm</br>: If the goal is to build a Base NN System and the main obstruction is the scaling of the learning algorithms, the solution would be to build a learning algorithm that doesn't scase exponentially with the complexity of the system. This is what this project is about - building that algorithm.
