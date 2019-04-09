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
LO_matrices: layer to output connections (SP system)
# weight_type[row][col]
# row -> source
# col -> target

Passed tests:
- Simple input  -> output relations

Still to pass:
- Varying input -> output relations | stucks on 0 or 1
- tictactoe, not tested
'''


def resist_factor(list_numb,resist_factor_kind):
    # - decreasing resist:
    if resist_factor_kind == 0:     # static resist 
        resistance = 100
    elif resist_factor_kind == 1:   # decreasing resist 
        resistance = 20 - list_numb*2
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
        self.input_size          = input_size
        self.hidden_size         = hidden_size
        self.output_size         = output_size
        self.hidden_count        = hidden_count
        # - Parameters:
        self.weight_type         = 3      # 0:(+=COV), 1:(mAve), 2:(X*F), 3:MA(X*F)
        self.max_resist          = 100    # Cell change max resistance
        self.resist_factor_kind  = 1      # 0:static, 1:decreasing
        self.min_PF              = 1      # PF/1000
        self.max_PF              = 999    # PF/1000
        self.step_PF             = 5      # Increase of PF/1000 every time cell doesn't fire
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
            temp_list = np.zeros(temp_size) #
            self.F_arrays_list.append(temp_list)
            temp_list = np.zeros(temp_size) #
            self.PF_arrays_list.append(temp_list)
            temp_list = np.zeros(temp_size) #
            self.EF_arrays_list.append(temp_list)
            temp_list = np.zeros(temp_size) #
            self.X_arrays_list.append(temp_list)
            temp_list = np.zeros(temp_size) #
            self.EX_arrays_list.append(temp_list)
            # -- Resist:
            temp_list = []
            temp_resist = resist_factor(list_numb,self.resist_factor_kind)
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
            temp_matrix = np.random.randint(-10, high=10, size=(temp_LL_in_size, temp_LL_out_size))
            temp_matrix = temp_matrix/100.
            self.LL_matrices_list.append(temp_matrix)
            # -- Create the LO matrices:
            if list_numb == 0:
                temp_LO_in_size  = self.input_size
                temp_LO_out_size = self.output_size
            else:
                temp_LO_in_size  = self.hidden_size
                temp_LO_out_size = self.output_size
            temp_matrix = np.random.randint(-10, high=10, size=(temp_LO_in_size, temp_LO_out_size))
            temp_matrix = temp_matrix/100.
            self.LO_matrices_list.append(temp_matrix)  
    # END INIT
    ##########


    ###################
    # INPUT AND UPDATE:
    def inputAndUpdate(self, input_array):
        for list_numb in range(self.hidden_count+2):
            # - reset Fs:
            for cell_numb in range(len(self.F_arrays_list[list_numb])):
                self.F_arrays_list[list_numb][cell_numb] = 0.
            # - reset PFs:
            for cell_numb in range(len(self.PF_arrays_list[list_numb])):
                self.PF_arrays_list[list_numb][cell_numb] = 0.
    
    
        for list_numb in range(self.hidden_count+2):                
            # - if input layer -> Get input
            if list_numb == 0:
                for cell_numb in range(len(self.F_arrays_list[0])):
                    self.PF_arrays_list[0][cell_numb] = input_array[cell_numb]
                    
            # - if hidden or input layer:
            if list_numb != self.hidden_count+1:
                for cell_numb in range(len(self.PF_arrays_list[list_numb])):
                    # -- bound normalize PFs (min < PF < max):
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
                        
            # - bound normalize PFs for output (min < OF):
            if list_numb == self.hidden_count+1:
                for cell_numb in range(len(self.PF_arrays_list[list_numb])):
                    PF = self.PF_arrays_list[list_numb][cell_numb]*1000
                    min_value = self.min_PF_arrays_list[list_numb][cell_numb]
                    PF = utils.boundInputMin(PF, min_value)
                    self.PF_arrays_list[list_numb][cell_numb] = PF/1000.
                
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
                self.PF_arrays_list[self.hidden_count+1] += PF 
                
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
    def feedback(self, feedback):
        # - X and EX:
        for list_numb in range(self.hidden_count+1):
            for cell_numb in range(len(self.X_arrays_list[list_numb])):
                # - Calculate X  = F * feedback
                self.X_arrays_list[list_numb][cell_numb] = self.F_arrays_list[list_numb][cell_numb]*feedback
                # - Calculate EX = movingAverage(X)
                old_value  = self.EX_arrays_list[list_numb][cell_numb]
                new_value  = self.X_arrays_list[list_numb][cell_numb]
                resistance = self.R_arrays_list[list_numb][cell_numb]
                EX = utils.movingAverage(old_value, new_value, resistance)
                self.EX_arrays_list[list_numb][cell_numb] = EX
    
        # - LL connections:
        for list_numb in range(self.hidden_count):
            for row in range(len(self.LL_matrices_list[list_numb])):
                for col in range(len(self.LL_matrices_list[list_numb][row])):
                    
                    # - COV(X,EX,F,EF) | X-source, F-target:
                    X  = self.X_arrays_list[list_numb][row]
                    EX = self.EX_arrays_list[list_numb][row]
                    F  = self.F_arrays_list[list_numb+1][col]
                    EF = self.EF_arrays_list[list_numb+1][col]
                    COV_ = utils.COV(X,EX,F,EF)
                
                    if self.weight_type ==0:
                        # - weight_type += COV_:
                        self.LL_matrices_list[list_numb][row][col] += COV_
                    
                    elif self.weight_type == 1:
                        # - weithg = movingAverage(COV_)
                        old_value  = self.LL_matrices_list[list_numb][row][col]
                        new_value  = COV_
                        resistance = self.R_arrays_list[list_numb][row]
                        self.LL_matrices_list[list_numb][row][col] = utils.movingAverage(old_value, new_value, resistance)

                    elif self.weight_type == 2:
                        # - weight_type = X*F:
                        self.LL_matrices_list[list_numb][row][col] += X*F
                        
                    elif self.weight_type == 3:
                        # - weight_type = movingAverage(X*F):
                        old_value  = self.LL_matrices_list[list_numb][row][col]
                        new_value  = X*F
                        resistance = self.R_arrays_list[list_numb][row]
                        self.LL_matrices_list[list_numb][row][col] = utils.movingAverage(old_value, new_value, resistance)
                        
        # - LO connections:
        for list_numb in range(self.hidden_count+1):
            for row in range(len(self.LO_matrices_list[list_numb])):
                for col in range(len(self.LO_matrices_list[list_numb][row])):
                    
                    # - COV(X,EX,F,EF) | X-source, F-target:
                    X  = self.X_arrays_list[list_numb][row]
                    EX = self.EX_arrays_list[list_numb][row]
                    F  = self.F_arrays_list[self.hidden_count+1][col]
                    EF = self.EF_arrays_list[self.hidden_count+1][col]
                    COV_ = utils.COV(X,EX,F,EF)
                
                    if self.weight_type == 0:
                        # - weight_type += COV_:
                        self.LO_matrices_list[list_numb][row][col] += COV_   
                    
                    elif self.weight_type == 1:
                        # - weithg = movingAverage(COV_)
                        old_value  = self.LO_matrices_list[list_numb][row][col]
                        new_value  = COV_
                        resistance = self.R_arrays_list[list_numb][row]
                        self.LO_matrices_list[list_numb][row][col] = utils.movingAverage(old_value, new_value, resistance)
                    
                    elif self.weight_type == 2:
                        # - weight_type = X*F:
                        self.LO_matrices_list[list_numb][row][col] += X*F
                        
                    elif self.weight_type == 3:
                        # - weight_type = movingAverage(X*F):
                        old_value  = self.LO_matrices_list[list_numb][row][col]
                        new_value  = X*F
                        resistance = self.R_arrays_list[list_numb][row]
                        self.LO_matrices_list[list_numb][row][col] = utils.movingAverage(old_value, new_value, resistance)
                        
                        
    # END FEEDBACK
    ##############
    
    ################
    # RETURN OUTPUT:
    def returnOutputPlace(self):
        layer_numb  = self.hidden_count+1
        cell_numb   = 0
        while cell_numb < self.output_size:
            if self.F_arrays_list[layer_numb][cell_numb] == 1:
                output_place = cell_numb
            cell_numb+=1
        return output_place    
    # END RETURN OUTPUT
    ###################
    
    
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
