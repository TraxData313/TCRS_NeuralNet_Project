import numpy as np
import random


##############
# - Class Cell:
# - Basic permutator based object
# - Has connections with other cells, which are used to build the input
# - Every input permuatation is a different input state
# - Uses the natural weight equation to determine its output given its input state
# - No distance metric between the different input states yet exists, hence this is a simple permutator unit

class Cell:
    def __init__(self,
                cell_type=0,
                cell_connections = [],
                cell_connections_numb = 3):
        self.cell_type = cell_type # 0=input, 1=hidden, 2=output
        self.firedBool = False
        self.cell_connections_numb = cell_connections_numb
        self.cell_connections = cell_connections
        self.inputs    = [False]*self.cell_connections_numb
        # - Make the list for the corresponding PF for each permutation (0<PF<1):
        self.PF_list = np.random.random(2**self.cell_connections_numb)
        # - Make the list of all input permutations (manual for now):
        self.permutations = []
        self.permutations.append([True,True,True])
        self.permutations.append([True,True,False])
        self.permutations.append([True,False,False])
        self.permutations.append([True,False,True])
        self.permutations.append([False,True,True])
        self.permutations.append([False,True,False])
        self.permutations.append([False,False,False])
        self.permutations.append([False,False,True])

    def get_input(self, bool_inputs):
        self.inputs = bool_inputs

    def process_input(self):
        pass # self.firedBool as a func of self.inputs
        # - Compare the input with the permutations and get its place:
        for i in range(2**self.cell_connections_numb):
            if self.inputs == self.permutations[i]:
                input_perm_place = i
        # - Fire or not with probability PF[i]:
        rand_int = random.randint(0,100)/100
        if self.PF_list[i] > rand_int:
            self.firedBool = True
        else:
            self.firedBool = False

    def __repr__(self):
        return "Type {} cell. Fired: {}".format(self.cell_type, self.firedBool)
# END Class Cell
################



###########################
# - Class SimplePermutator:
# - Creates a permutator object, which houses cells
# - Manages the syncronization of the cells
# - NOTE: Reward ranges from 0 to 1, where 0 is most negative, 0.5 is neutral, and 1 is most positive

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
        self.cell_connections_numb = 3

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
                temp_connections = []
                # - if first layer:
                if i == 0:
                    for k in range(self.input_size):
                        temp_connections.append(random.randint(0,self.input_size-1))
                # - for other layers:
                else:
                    for k in range(self.hidden_size):
                        temp_connections.append(random.randint(0,self.hidden_size-1))
                temp_hidden_cells_list.append(Cell(cell_type=1, cell_connections = temp_connections))
                print("Hidden connections:", temp_hidden_cells_list[j].cell_connections)
            self.hidden_cells.append(temp_hidden_cells_list)

        # -- Populate the output cells:
        for i in range(self.output_size):
            temp_connections = []
            if self.hidden_count == 0:
                for k in range(self.input_size):
                    temp_connections.append(random.randint(0,self.input_size-1))
                self.output_cells.append(Cell(cell_type=2, cell_connections = temp_connections))
                print("Output connections:", self.output_cells[i].cell_connections)
            else:
                for k in range(self.hidden_size):
                    temp_connections.append(random.randint(0,self.hidden_size-1))
                self.output_cells.append(Cell(cell_type=2, cell_connections = temp_connections))
                print("Output connections:", self.output_cells[i].cell_connections)

        i = i # supress anoying problem popup that i is not used!
        j = j
        k = k
    # END INIT
    ##########


    ##########
    # METHODS:
    # - get_input
    # - propagate_signal
    # -- cell.get_input
    # -- cell.process_input
    # - read_output_state
    # - read_output_prob
    # - process_reward

    def get_input(self, bool_vector):
        if len(bool_vector) != self.input_size:
            print()
            print("ERROR: Input bool vector size does not match the input size for this permutator!")
            print("- input bool vector size:", len(bool_vector))
            print("- permutator  input_size:", self.input_size)
            print('- input bool vector contents:', bool_vector)
            print("- program will brake now...")
            print()
        for i in range(self.input_size):
            self.input_cells[i].firedBool = bool_vector[i]

    # - propagate_signal:
    def propagate_signal(self):
        # -- propagate hidden cells:
        for i in range(self.hidden_count):
            for j in range(self.hidden_size):
                bool_inputs = [True, False, True]
                # -- cell.get_input:
                self.hidden_cells[i][j].get_input(bool_inputs)
                # -- cell.process_input:
                self.hidden_cells[i][j].process_input()
        # -- propagate output cells:
        for i in range(self.output_size):
            # -- cell.get_input:
            self.output_cells[i].get_input(bool_inputs)
            # -- cell.process_input:
            self.output_cells[i].process_input()
                
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






