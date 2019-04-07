# Structure and Mechanics:
- The network is made from layers of cells and connections between the layers
- Every layer is connected to the output layer (Spinal Cord System)
- Every cell fires or doesn't fire
- The probability of fire is calcilated using the connected cells and their weights
- Every cell keeps statistical data about its Fire Friquency and Fire*Feedback relation

# Static:
- The Neural Network can deal with static situations, where the desigion at every state is not dependend on the past states
- Example: playing a game of tic-tac-toe or a game of chess

# Covariant Feedback System:
- Every connection is transformed as a function of the covarience between the source cell FireState*Feedback and the target cell FireState
- - If the source cell tends to notice negative feedback when a given target cell has fired, it learns to prevent the target cell from firing
- - If the source cell tends to notice positive feedback when a given target cell has fired, it learns to encourage the target cell to fire
