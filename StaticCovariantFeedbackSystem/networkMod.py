import numpy as np
import random
import time
import utils


'''
Cell properties:
F : fired = 1 or 0
PF: prob of fire
EF: moving average of F
X : fired*feedback
EX: moving average of X
R : moving averages change resistance
min_PF: min prob of fire

Matrices:
LL_matrices: layer to layer connections
LO_matrices: layer to output connections

Simulation problem: every time you add a layer of symulation the run time of the system increasex with exp(complexityOfTheSystem)

Neural networks are being simulated on out machines

Solution: build a neural net, not a simulation that can run on our machines
'''


def resist_factor(list_numb,resist_factor_kind):
    # - decreasing resist:
    if resist_factor_kind == 1:
        resistance = 100 - list_numb*10
    return resistance
        





################
# Class Network:
class Network:

    #######
    # INIT:
    def __init__(self,
                 input_size,
                 hidden_size,
                 output_size,
                 hidden_count):
        # - Dimentions:
        self.input_size        = input_size
        self.hidden_size       = hidden_size
        self.output_size       = output_size
        self.hidden_count      = hidden_count
        # - Parameters:
        self.starting_resist   = 5      # Cell change min resistance
        self.max_resist        = 100    # Cell change max resistance
        self.min_PF            = 300    # PF/1000
        self.max_PF            = 990    # PF/1000
        self.step_PF           = 10     # Increase of PF/1000
        # - Cell properties in Arrays: F, PF, EF, X, EX, R, min_PF:
        self.F_arrays_list       = []
        self.PF_arrays_list      = []
        self.EF_arrays_list      = []
        self.X_arrays_list       = []
        self.EX_arrays_list      = []
        self.R_arrays_list       = []
        self.min_PF_arrays_list  = [] # P = min_PF/1000
        for list_numb in range(self.hidden_count+2):
            if list_numb == 0:
                temp_size = self.input_size
            elif list_numb == self.hidden_count+1:
                temp_size = self.output_size
            else:
                temp_size = self.hidden_size
            temp_list = np.zeros(temp_size)
            self.F_arrays_list.append(temp_list)
            self.PF_arrays_list.append(temp_list)
            self.EF_arrays_list.append(temp_list)
            self.X_arrays_list.append(temp_list)
            self.EX_arrays_list.append(temp_list)
            # -- Resist:
            temp_list = []
            resist_factor_kind = 1
            temp_resist = resist_factor(list_numb,resist_factor_kind)
            for n in range(temp_size):
                temp_list.append(temp_resist)
            self.R_arrays_list.append(temp_list)
            # -- min_PF:
            temp_list = []
            for n in range(temp_size):
                temp_list.append(self.min_PF)
            self.min_PF_arrays_list.append(temp_list)
        # - Connection Matrices:
        self.LL_matrices_list = []
        self.LO_matrices_list = []
        for list_numb in range(hidden_count+1):
            # -- Create the LL matrices:
            if list_numb == 0:
                temp_LL_in_size  = self.input_size
                temp_LL_out_size = self.hidden_size
            elif list_numb == hidden_count:
                temp_LL_in_size  = 0
                temp_LL_out_size = 0
            else:
                temp_LL_in_size  = self.hidden_size
                temp_LL_out_size = self.hidden_size
            temp_matrix = np.zeros((temp_LL_in_size, temp_LL_out_size))
            self.LL_matrices_list.append(temp_matrix)
            # -- Create the LO matrices:
            if list_numb == 0:
                temp_LO_in_size  = self.input_size
                temp_LO_out_size = self.output_size
            else:
                temp_LO_in_size  = self.hidden_size
                temp_LO_out_size = self.output_size
            temp_matrix = np.zeros((temp_LO_in_size, temp_LO_out_size))
            self.LO_matrices_list.append(temp_matrix)  
    # END INIT
    ##########


    ###################
    # INPUT AND UPDATE:
    def inputAndUpdate(self, input_array):
        for list_numb in range(self.hidden_count+2):
            print(" ")
            print("LIST:", list_numb)
            
            # - reset Fs:
            for cell_numb in range(len(self.F_arrays_list[list_numb])):
                self.F_arrays_list[list_numb][cell_numb] = 0.
                
            # - if input layer -> Get input
            if list_numb == 0:
                for cell_numb in range(len(self.F_arrays_list[0])):
                    self.PF_arrays_list[0][cell_numb] = input_array[cell_numb]
                    
            # - if hidden or input layer:
            if list_numb != self.hidden_count+1:
                for cell_numb in range(len(self.PF_arrays_list[list_numb])):
                    # -- bound normalize PFs:
                    PF = self.PF_arrays_list[list_numb][cell_numb]*1000
                    min_value = self.min_PF_arrays_list[list_numb][cell_numb]
                    max_value = self.max_PF
                    PF = utils.boundInputMinMax(PF, min_value, max_value)
                    self.PF_arrays_list[list_numb][cell_numb] = PF/1000.
                    # -- Decide whether to fire based on PF:
                    randNumb = random.randint(0,1000)
                    if randNumb <= PF:
                        self.F_arrays_list[list_numb][cell_numb] = 1
                        # -- if fired  -> min_PF  = min_PF :
                        self.min_PF_arrays_list[list_numb][cell_numb] = self.min_PF 
                    else:
                        self.F_arrays_list[list_numb][cell_numb] = 0
                        # -- if !fired -> min_PF += step_PF :
                        self.min_PF_arrays_list[list_numb][cell_numb] += self.step_PF  
                
            # - Run LL connections PF(n+1) = F(n) * LL : 
            if list_numb < self.hidden_count:
                PF = self.PF_arrays_list[list_numb+1]
                F  = self.F_arrays_list[list_numb]
                LL = self.LL_matrices_list[list_numb]
                self.PF_arrays_list[list_numb+1] = np.dot(F, LL)
             
            # - Run LO connections PF(out) += F(n) * LO :
            if list_numb < self.hidden_count+1:
                PF = self.PF_arrays_list[self.hidden_count+1] # target = output layer
                F  = self.F_arrays_list[list_numb]
                LO = self.LO_matrices_list[list_numb]
                PF = np.dot(F, LO)
                self.PF_arrays_list[self.hidden_count+1] += PF # need to test this!
                
            # - if output layer -> provide the output O(PF)
            if list_numb == self.hidden_count+1:
                sum = 0
                cell_numb = 0
                while cell_numb < self.output_size:
                    sum += self.PF_arrays_list[list_numb][cell_numb]
                    cell_numb+=1
                sum = sum*1000
                sum = int(sum)
                randInt = random.randint(0,sum)
                cell_numb    = 0
                winner       = 0
                runnning_sum = 0
                while winner == 0:
                    runnning_sum += self.PF_arrays_list[list_numb][cell_numb]*1000
                    if randInt <= runnning_sum:
                        self.F_arrays_list[list_numb][cell_numb] = 1
                        winner = 1
                    cell_numb+=1
                
            # - update EF:
            for cell_numb in range(len(self.EF_arrays_list[list_numb])):
                # -- EF = movingAverage(F)
                old_value  = self.EF_arrays_list[list_numb][cell_numb]
                new_value  = self.F_arrays_list[list_numb][cell_numb]
                resistance = self.R_arrays_list[list_numb][cell_numb]
                EF = utils.movingAverage(old_value, new_value, resistance)
                self.EF_arrays_list[list_numb][cell_numb] = EF
            
    # END INPUT AND UPDATE
    ######################
    
    
    ###########
    # FEEDBACK:
    def feedback(self):
        # - Calculate X  = F * feedback
        # - Calculate EX = movingAverage(X)
        # - For every connection:
        # -- Recover the source and target
        # -- weight = movingAverage(COV) | COV1 = (X-EX)*(F-EF) , COV2 = (X)*(F-EF)
        pass
    
    # END FEEDBACK
    ##############
    
    
    ###########
    # PRINTERS:
    def __repr__(self):
        return "N: {} -> {}x{} -> {}".format(self.input_size, 
                                            self.hidden_count, 
                                            self.hidden_size,
                                            self.output_size)
    # END PRINTERS
    ##############
    
# END Class Newtork
################### 
