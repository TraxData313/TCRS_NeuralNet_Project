import numpy as np
import random
import time
import utilsDemo


'''
GLOBAL RULES:
- Standard ANN connection topology

LOCAL RULES:
- w(a,b) += a*b*reward 
'''







##################
# Class Network:
class Network:
    
    #######
    # INIT:
    def __init__(self,
                 input_size,
                 hidden_size,
                 output_size,
                 hidden_count,
                 is_RNN=0):
        # - Dimentions:
        self.hidden_count = hidden_count
        self.input_size   = input_size
        self.hidden_size  = hidden_size
        self.output_size  = output_size
        
        # - Parameters:
        self.is_RNN = is_RNN    # 0=ANN, 1=RNN - NOTE: RNN doesn't work here!
        self.RNN_reduce = 0.5   # on every turn reduce/weaken the PFs (0.5 reduces by 1/2)
        self.min_PF = 0.005
        self.max_PF = 0.995
        self.init_EF_resist   = 0
        self.max_EF_resist    = 100000
        self.D_resist         = 500   # stationary connection resistance
        
        # - Variables:
        self.life = 0
        self.EF_resist = self.init_EF_resist
        
        # - Declare the cell layers:
        self.F_list  = [] # F  : Fired/notFired : 1/0
        self.PF_list = [] # PF : Prob(Fire)
        self.EF_list = [] # EF : MovingAverage(Fire)
        self.R_list  = [] # R  : Fire*Reward
        self.ER_list = [] # ER : MovingAverage(Fire*Reward)
        
        # - Populate the cell layers:
        # -- Populate the input layers:
        temp_array = np.zeros(input_size)
        self.F_list.append(temp_array)
        temp_array = np.zeros(input_size)
        self.PF_list.append(temp_array)
        temp_array = np.zeros(input_size)
        self.EF_list.append(temp_array)
        temp_array = np.zeros(input_size)
        self.R_list.append(temp_array)
        temp_array = np.zeros(input_size)
        self.ER_list.append(temp_array)
        # -- Populate the hidden layers:
        for n in range(hidden_count):
            temp_array = np.zeros(hidden_size)
            self.F_list.append(temp_array)
            temp_array = np.zeros(hidden_size)
            self.PF_list.append(temp_array)
            temp_array = np.zeros(hidden_size)
            self.EF_list.append(temp_array)
            temp_array = np.zeros(hidden_size)
            self.R_list.append(temp_array)
            temp_array = np.zeros(hidden_size)
            self.ER_list.append(temp_array)
        
        # - Create the output layer:
        self.output_PF = np.zeros(output_size)
        self.output_F  = [] 
        
        # - Declare the connection matrices lists and the connection memory:
        self.LLC_list = [] # Layer-to-Layer      Connection matrices | List(Matrices)
        self.LOC_list = [] # Layer-to-Output     Connection matrices | List(Matrices)
        
        # - Populate the LLC_list:
        for n in range (hidden_count):
            rows = len(self.F_list[n])
            cols = len(self.F_list[n+1])
            # - Connections:
            temp_matrix = utilsDemo.diagonalized(rows, cols, min=-0.2, max=0.2)
            self.LLC_list.append(temp_matrix)
        
        # - Populate the LOC_list:
        for n in range (hidden_count+1):
            rows = len(self.F_list[n])
            cols = len(self.output_PF)
            temp_matrix = utilsDemo.diagonalized(rows, cols, min=-0.2, max=0.2)
            self.LOC_list.append(temp_matrix)
    # END INIT
    ##########
    
    
    ############
    # Operators:

    ### ### ###
    ### Get Input and Propagate:
    
    # ROADMAP for Input and Propagate:
    # - Reset Fs
    # - Reset PFs and output layer
    # - Iterate all layers:
        # -- For layer == 0: 
            # --- get input into PF
            # --- F = PF
        # -- For layer  > 0: 
            # --- decide whether to F | PF
        # -- Run LL connections PF[n+1]   += F[n] * LL[n]
    # - Run LO connections PF[out] += F[n] * LO[n]
    # - Update all EFs
    # - Increase the EF_resist
    # - Provide the output
    
    # IMPLEMENTATION of Input and Propagate:
    def getInputAndPropagate(self,input_array):
        # - Reset Fs:
        for layer in range(self.hidden_count+1):
            self.F_list[layer] = np.zeros(len(self.F_list[layer]))
            
        # - Reset PFs and output layer0:
        for layer in range(self.hidden_count+1):
            self.PF_list[layer] = np.zeros(len(self.PF_list[layer]))
        self.output_PF = np.zeros(self.output_size)
            
        # - Iterate all layers:
        for layer in range(self.hidden_count+1):
            # -- For layer == 0:
            if layer == 0:
                # --- get input into PF:
                self.PF_list[layer] = input_array
                # --- F = PF:
                self.F_list[layer] = self.PF_list[layer]
            # -- For layer  > 0: 
            if layer  > 0:
                # --- decide whether to F | PF:
                self.F_list[layer] = utilsDemo.fireNotFire(self.PF_list[layer], self.min_PF, self.max_PF)
            # -- Run LL connections PF[n+1]   += F[n] * LL[n]
            for n in range(self.hidden_count):
                self.PF_list[n+1] += np.dot(self.F_list[n], self.LLC_list[n])

        # - Run LO connections PF[out] += F[n] * LO[n]
        for n in range(self.hidden_count+1):
            PF_target = self.output_PF
            F_source  = self.F_list[n]
            LO_matrix = self.LOC_list[n]
            PF_target += np.dot(F_source, LO_matrix)
        
        # - Update all EFs:
        for layer in range(self.hidden_count+1):
            for el in range(len(self.F_list[layer])):
                old_value = self.EF_list[layer][el]
                new_value = self.F_list[layer][el]
                resistance = self.EF_resist
                self.EF_list[layer][el] = utilsDemo.movingAverage(old_value, new_value, resistance)
        
        # - Increase the EF_resist:
        self.EF_resist += 1
        if self.EF_resist > self.max_EF_resist:
            self.EF_resist = self.max_EF_resist
            
        # - Provide the output:
        self.output_F = utilsDemo.classOutput(self.output_PF, self.min_PF, self.max_PF)
    ### END Get Input and Propagate
    ### ### ###
   
    ### ### ###
    ### Get Reward and Update:
    
    # ROADMAP for Reward and Update:
    # - Calculate the Rs (skipping ERs for now)
    # - For all connection matrices:
        # -- Update the weight
        
    # IMPLEMENTATION of Reward and Update:
    def rewardAndUpdate(self, reward):
        
        # - Calculate the Rs:
        for layer in range(self.hidden_count+1):
            for el in range(len(self.R_list[layer])):
                self.R_list[layer][el] = self.F_list[layer][el] * reward
                
        # - For all connection matrices:
        # -- LLC_list, PF[n+1] += F[n] * LL[n]:
        for n in range(self.hidden_count):
            # -- Update the weights:
            for row in range(len(self.F_list[n])):
                R1 = self.R_list[n][row]
                for col in range(len(self.F_list[n+1])):
                    F2 = self.F_list[n+1][col]
                    self.LLC_list[n][row][col] += R1*F2
            
        # -- LOC_list, PF[out] += F[n] * LO[n]
        for n in range(self.hidden_count+1):
            # -- Update the weights:
            for row in range(len(self.F_list[n])):
                R1 = self.R_list[n][row]
                for col in range(len(self.output_F)):
                    F2 = self.output_F[col]
                    self.LOC_list[n][row][col] += R1*F2
    
    ### END Get Reward and Update
    ### ### ###
    
    ### ### ###
    ### returnOutputPlace:
    def returnOutputPlace(self):
        for n in range(self.output_size):
            if self.output_F[n] == 1:
                output_place = n        
        return output_place
    
    ### END returnOutputPlace
    ### ### ###
    
    # END Operators
    ###############

    
    #################
    # Representators:
    # - __repr__:
    def __repr__(self):
        return "NN dims: {} -> {}x{} -> {}".format(self.input_size, 
                                                    self.hidden_count, 
                                                    self.hidden_size,
                                                    self.output_size)
    # - Print cell layers:
    def printFlist(self):
        print()
        print("- Current Fired cells:")
        for n in range(self.hidden_count+1):
            print(self.F_list[n])
    def printPFlist(self):
        print()
        print("- Current Probability of Fire:")
        for n in range(self.hidden_count+1):
            print(self.PF_list[n])
    def printEFlist(self):
        print()
        print("- Average Fire State:")
        for n in range(self.hidden_count+1):
            print(self.EF_list[n])
    def printRlist(self):
        print()
        print("- Rewarded Cells:")
        for n in range(self.hidden_count+1):
            print(self.R_list[n])
    def printERlist(self):
        print()
        print("- Average Reward:")
        for n in range(self.hidden_count+1):
            print(self.ER_list[n])
    def printOutputLayer(self):
        print()
        print("- Output Layer PF and F:")
        print(self.output_PF)
        print(self.output_F)
    # - Print connection matrices:
    def printLLClist(self):
        print()
        print("- LLC matrices:")
        for n in range(self.hidden_count):
            print(self.LLC_list[n])
            print()
    def printLOClist(self):
        print()
        print("- LOC matrices:")
        for n in range(self.hidden_count+1):
            print(self.LOC_list[n])
            print()
    # END Representators
    ####################


# END Class Network
#####################










































