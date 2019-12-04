import numpy as np


##############
# - Class Cell:
# - Basic permutator based object
# - Has connections with other cells, which are used to build the input
# - Every input permuatation is a different input state
# - Uses the natural weight equation to determine its output given its input state
# - No distance metric between the different input states yet exists, hence this is a simple permutator unit

class Cell:
    def __init__(self,
                cell_type=0):
        self.cell_type = cell_type # 0=input, 1=hidden, 2=output
        self.firedBool = 0
        self.PF = 0 # Probability of firing (0 < PF < 1)

    def __repr__(self):
        return "Type {} cell in {} state".format(self.cell_type, self.firedBool)
# END Class Cell
################



###########################
# - Class SimplePermutator:
# - Creates a permutator object, which houses cells
# - Manages the syncronization of the cells

class SimplePermutator():

    #######
    # INIT:
    def __init__(self, 
                input_size=1, 
                hidden_size=1,
                hidden_count=0, 
                output_size=1):
        self.input_size   = input_size
        self.hidden_size  = hidden_size
        self.hidden_count = hidden_count
        self.output_size  = output_size
        self.cell_connections = 4

        # - Create the cell lists:
        self.input_cells  = []
        self.hidden_cells = [] # NOTE: This is a list of lists (hidden_count x hidden_size)
        self.output_cells = []

        # -- Populate the input cells:
        for i in range(self.input_size):
            self.input_cells.append(Cell(0))

        # -- Populate the hidden cells:
        for i in range(self.hidden_count):
            temp_hidden_cells_list = []
            for j in range(self.hidden_size):
                temp_hidden_cells_list.append(Cell(1))
            self.hidden_cells.append(temp_hidden_cells_list)

        # -- Populate the output cells:
        for i in range(self.output_size):
            self.output_cells.append(Cell(2))

    # END INIT
    ##########


    ##########
    # METHODS:
    # - get_input
    # - propagate_signal
    # - read_output_state
    # - read_output_prob
    # - process_reward

    def get_input(self, bool_vector):
        pass

    def propagate_signal(self):
        pass

    def read_output_state(self):
        pass
    
    def read_output_prob(self):
        pass

    def process_reward(self, reward):
        pass
    # END METHODS
    #############


    #################
    # Representators:
    # - __repr__
    # - printCells

    def __repr__(self):
        return "Simple Permutaror: {} -> {}x{} -> {}".format(self.input_size, 
                                             self.hidden_count, 
                                             self.hidden_size,
                                             self.output_size)
    def printCells(self):
        print()
        print("- Input cells:")
        for i in range(self.input_size):
            print("   ", self.input_cells[i])
        for i in range(self.hidden_count):
            print()
            print("- Hidden layer", i, "cells:")
            for j in range(self.hidden_size):
                print("   ", self.hidden_cells[i][j])
        print()
        print("- Output cells:")
        for i in range(self.output_size):
            print("   ", self.output_cells[i])
    # END Representators
    ####################

# END Class SimplePermutator
############################






