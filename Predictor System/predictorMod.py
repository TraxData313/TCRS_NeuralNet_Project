import numpy as np
import random
import time
import utils

'''
STRUCTURE:
- Diagonalized Connection Matrices
- Pull-Run Update process
- 2x2 network, first col = InputStack
- Separate Input[0] Cell
- Separate Output Array -> PredictionStack
LOOP:
- D[n] predicts I[0] -> matrix of predictions P
- Get Output/Prediction = SUM(P[n]*R[n])/SUM(R[n]) -> Output[0]
- get new input -> I[0]
- R[n] = 1/(P[n]-I[0])^2 -> matrix of ratings R
SIMULATION:
- Run n simulations using Output[n] as Input[0] to get Output[n+1] 
DETAILS:
- Encode Dendrite:
	Dn = E(COV) = E((I[0]-EI[0])*(A[n]-EA[n]))
- Decode Dendrite:
	Dn = (I[0]-EI[0])*(A[n]-EA[n])
	Dn = I0*An - I0*EAn - EI0*An + EI0*EAn
	Dn = I0(An - EAn) - EI0*An + EI0*EAn
	Dn - I0(An - EAn) = - EI0*An + EI0*EAn
	- I0(An - EAn) = - EI0*An + EI0*EAn - Dn
	I0(An - EAn) = EI0*An - EI0*EAn + Dn
	I0 = (EI0*An - EI0*EAn + Dn)/(An - EAn)
	set:
	Pn = I0
	check: if EI0 = EAn = 0 -> I0 = Dn/An   (correct)
- Compare Pn with real I0 to get rating Rn
	Rn = 1 / (I0-Pn)^2
- Total predictions TP:
	TP = SUM(Pn*Rn)/SUM(Rn)
- Prediction error per cell:
	Error n = En = I0-Pn
	if I0 = 1 and Pn = 0.7 -> En = 0,3
	get average of En and add En to the Pn next time
	if on average the Cell undershoots -> it will get start giving higher Pn
'''

##################
# Class Predictor:
class Predictor:

    #######
    # INIT:
    def __init__(self,
                 row_count,
                 row_size):
                
        # - Dimentions:
        self.row_size    = row_size
        self.row_count   = row_count
        self.output_size = 1
        
        # - Parameters:
        self.life                = 0
        self.min_resist          = 0
        self.max_resist          = 1000
        self.pull                = 1   # if 1: Pull-Run, if 0: Push-Run
        self.dendr_type          = 0   # 0: E(COV)
        
        # - Create the input cell:
        self.input_cell          = 0.
        
        # - Create the output (prediction) layer:
        self.output_layer = np.zeros(self.output_size)
        
        # - Create the cell_matrices:
        self.cell_matrix_V       = np.zeros((row_count, row_size)) # Value
        self.cell_matrix_EV      = np.zeros((row_count, row_size)) # E(V)
        self.cell_matrix_D       = np.zeros((row_count, row_size)) # Dendrite
        self.cell_matrix_R       = np.zeros((row_count, row_size)) # Resistance
        self.cell_matrix_E       = np.zeros((row_count, row_size)) # Prediction Error
        for row in range(row_count):
            for el in range(row_size):
                self.cell_matrix_R[row][el] = self.min_resist
        
        # - Create the connection matrices:
        self.connections_list    = []
        
        # - Populate with diagnolized matrices:
        for n in range(row_count-1):
            temp_matrix = utils.diagonalized(row_size, row_size)
            self.connections_list.append(temp_matrix)
    # END INIT
    ##########


    ###################
    # INPUT AND UPDATE:
    def inputAndUpdate(self, new_input):
        
        # - Get the input to the input cell:
        self.input_cell = new_input
        
        # - Update the dendrites:
        if self.life > self.row_size:
            for row in range(self.row_count):
                for el in range(self.row_size):
                    if self.dendr_type == 0:
                        # Dn = E(COV) = E((I[0]-EI[0])*(A[n]-EA[n]))
                        # -- Recover the needed variables:
                        Dn  = self.cell_matrix_D[row][el]
                        I0  = self.input_cell
                        EI0 = self.cell_matrix_EV[0][0]
                        An  = self.cell_matrix_V[row][el]
                        EAn = self.cell_matrix_EV[row][el]
                        # -- Calculate the covariance:
                        COV_ = utils.COV(I0,EI0,An,EAn)
                        # -- Calculate and set Dn = E(COV):
                        old_value  = Dn
                        new_value  = COV_
                        resistance = self.cell_matrix_R[row][el]
                        Dn = utils.movingAverage(old_value, new_value, resistance)
                        self.cell_matrix_D[row][el] = Dn
        
        # - Move Input array back:
        for el in range(self.row_size-1):
            self.cell_matrix_V[0][-1-el] = self.cell_matrix_V[0][-2-el]
        
        # - Set A[0][0] = input:
        self.cell_matrix_V[0][0] = self.input_cell
        
        # - Run connections:
        if self.pull == 1:
            self.cell_matrix_V = utils.runConnectionsPull(self.cell_matrix_V,
                                                          self.connections_list)
        else:
            self.cell_matrix_V = utils.runConnectionsPush(self.cell_matrix_V,
                                                          self.connections_list)
        # line stopper
        
        # - Update the EVs and Rs:
        for row in range(self.row_count):
            for el in range(self.row_size):
                # -- EVs:
                old_value  = self.cell_matrix_EV[row][el]
                new_value  = self.cell_matrix_V[row][el]
                resistance = self.cell_matrix_R[row][el]
                self.cell_matrix_EV[row][el] = utils.movingAverage(old_value, new_value, resistance)
                # -- Rs:
                self.cell_matrix_R[row][el] += 1
                if self.cell_matrix_R[row][el] > self.max_resist:
                    self.cell_matrix_R[row][el] = self.max_resist
        
        # - Update life:
        self.life += 1
    # END INPUT AND UPDATE
    ######################
    
    
    ##########
    # PREDICT:
    def predict(self):
        pass
        # - Reconstruct next input:
        # Pn = (EI0*An - EI0*EAn + Dn)/(An - EAn)
        # Prediction = SUM(Pn*Rn)/SUM(Rn)
    # END PREDICT
    #############
    
    
    ###########
    # PRINTERS:
    # - Standard Repr:
    def __repr__(self):
        return "Predictor of size {}x{}".format(self.row_size, 
                                                self.row_count)
    
    # - Connections:
    def printConnections(self):
        print()
        print("Connection matrices:")
        for n in range(self.row_count-1):
            print(n)
            print(self.connections_list[n])
            
    # - Cell values:
    def printValues(self):
        print()
        print("Cell values:")
        for n in range(self.row_count):
            print(self.cell_matrix_V[n])
            
    # - Cell average values:
    def printAveValues(self):
        print()
        print("Cell average values:")
        for n in range(self.row_count):
            print(self.cell_matrix_EV[n])
            
    # - Cell change resistances:
    def printResistances(self):
        print()
        print("Cell change resistances:")
        for n in range(self.row_count):
            print(self.cell_matrix_R[n])
            
    # - Cell change resistances:
    def printDendrites(self):
        print()
        print("Cell dendrites:")
        for n in range(self.row_count):
            print(self.cell_matrix_D[n])
    # END PRINTERS
    ##############
    
# END Class Predictor
#####################