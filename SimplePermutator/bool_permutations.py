import numpy as np

def bool_permutations(vector_size=2):
    """Returns the list of all possible boolean permutations for a vector of size vector_size.
    The number of permutations returned = 2^vector_size
    
    Ex:
    vector_size = 2, returns:
    [True , True]
    [False, True]
    [True , False]
    [False, False]
    
    total of 2^2 = 4 permutations
    """
    # - Calculate the number of permutations:
    perm_count = 2**vector_size
    # - Initiate he permutations list:
    permutations = []
    for perm_numb in range(perm_count):
        temp_perm = []
        permutations.append(temp_perm)
    # - Do the append passes:
    for append_pass in range(vector_size):
        bool_value = False
        for list_numb in range(perm_count):
            if (list_numb)%(2**append_pass) == 0:
                bool_value = not(bool_value)
            permutations[list_numb].append(bool_value)
    return permutations