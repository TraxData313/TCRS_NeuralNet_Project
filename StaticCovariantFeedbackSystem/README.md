# Structure and Mechanics:
- The network is made from layers of cells and connections between the layers
- Every cell fires or doesn't fire
- The probability of fire is calcilated using the connected cells and their weights
- Every cell keeps statistical data about its Fire Friquency and Fire*Feedback relation
- The Spinal Cord System ensures smooth increase of performance over time (Every layer is connected to the output, not just the last layer. SCS is the system that manages that.)

# Static:
- The Neural Network can deal with static situations, where the desigion at every state is not dependend on the past states
- Example: playing a game of tic-tac-toe or a game of chess

# Covariant Feedback System:
- Every connection is transformed as a function of the covarience between the source cell FireState*Feedback and the target cell FireState
- - If the source cell tends to notice negative feedback when a given target cell has fired, it learns to prevent the target cell from firing
- - If the source cell tends to notice positive feedback when a given target cell has fired, it learns to encourage the target cell to fire

# Passes:
- Simple test        : Constant Answer  (output = 0,1 const)
- Basic test         : Dependent Answer (if input=0,1, output = 0,1, if input = 1,0, output = 1,0)
- Naive Classifiers  : Answer as a function of position, but not on correlations between coordinates
- Simple General Classifier : Answer depends not only on position, but also on correlations between coordinates

# Next goals:
- Solving the Complex Genral Classifiers: Those problems require bigger networks, and this basic TCRS is trying to modify all the weights at once, which causes "confisuion".

# Solution:
- Solution in order to move on to the Simple General Clasifier: <b>LB_matrices</b>. In order to solve this problem (avoiding the trivial brute force solutions, like gradien decent), I had to give the ability for the Layer n+1 cells to suppress the Layer n cells.
