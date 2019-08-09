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

####################
# - decodeDendrites:
def decodeDendrites(dendr_matrix, 
                    value_matrix, 
                    averages_matrix,
                    dendr_rating_matrix):
    '''
    OPERATION:
    For Pre-Encoded Dn = E(COV) = E((I[0]-EI[0])*(A[n]-EA[n]))
    Decoding: Pn = (EI0*An - EI0*EAn + Dn)/(An - EAn) =
    = (EI0(An - EAn) + Dn)/(An - EAn) =
    = EI0 + Dn/(An - EAn)
    Prediction = SUM(Pn*Rn)/Rn
    WHERE:
    Dn:  n'th Dendrite
    Rn:  n'th Dendrite Rating
    Pn:  n'th Prediction
    An:  n'th Current Value
    EAn: Moving Average of An
    EI0: Moving Average of A0 (first input)
    '''
    rows = len(dendr_matrix)
    cols = len(dendr_matrix[0])
    # - Decode the dendrites into the Pn's:
    Pred_matrix = np.zeros((rows, cols))
    for row in range(rows):
        for el in range(cols):
            # Pn = EI0 + Dn/(An - EAn)
            Pred_matrix[row][el] = averages_matrix[0][0]
            divisor = (value_matrix[row][el] - averages_matrix[row][el])
            if divisor == 0:
                print()
                print("BIG FAIL: divisor = 0 in decodeDendrites ... O.O")
                print()
                print("- You said you will take care of this when it happens,")
                print("  well... It happened! Time to deal with it!")
                print()
                print("Reminder: set every nan element to 0 and")
                print("          its rating to 0")
                print()
                hophop = 1/0
            else:
                Pred_matrix[row][el] += dendr_matrix[row][el]/divisor
    # - Return the prediction = SUM(Pn*Rn)/Rn:
    return Pred_matrix, np.sum(np.multiply(Pred_matrix, dendr_rating_matrix)) / np.sum(dendr_rating_matrix)
# END decodeDendrites
#####################


##################
# Class Predictor:
class Predictor:

    #######
    # INIT:
    def __init__(self,
                 row_count,
                 row_size,
                 output_size):
                
        # - Dimentions:
        self.row_size    = row_size
        self.row_count   = row_count
        self.output_size = output_size
        
        # - Parameters:
        self.min_V_resist        = 0
        self.max_V_resist        = 1    # max_V_resist = 1 : COV -> dX/dY
        self.min_D_resist        = 0
        self.max_D_resist        = 1000
        self.dRating_resist      = 100  # Rating resist
        self.pull                = 1    # if 1: Pull-Run, if 0: Push-Run
        self.dendr_type          = 0    # 0: E(COV)
        self.start_predicting    = 10
        self.mainR_resist        = 10   # Resistance for the output rating
        
        # - Variables:
        self.life                = 0
        self.RV                  = self.min_V_resist # Value    change resistance
        self.RD                  = self.min_D_resist # Dendrite change resistance
        
        # - Create the input cell:
        self.input_cell          = 0.
        
        # - Create the output (prediction) layer:
        self.output_layer  = np.zeros((self.output_size, self.output_size))
        
        # - Create the prediction error layer:
        self.error_layer   = np.zeros(self.output_size)
        
        # - Create the cell_matrices:
        self.cell_matrix_V       = np.zeros((row_count, row_size)) # Value
        self.cell_matrix_EV      = np.zeros((row_count, row_size)) # E(V)
        self.cell_matrix_D       = np.zeros((row_count, row_size)) # Dendrite
        self.cell_matrix_P       = np.zeros((row_count, row_size)) # Last Prediction
        self.cell_matrix_DR      = np.ones((row_count, row_size))  # Dendrite Rating
        self.cell_matrix_ER      = np.zeros((row_count, row_size)) # Average Cell Prediction Error
        
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
        
        # - Evaluate the prediction:
        if self.life > self.start_predicting+1:
            for n in range(self.output_size):
                old_value  = self.error_layer[n]
                new_value  = abs((self.output_layer[n][n] - self.input_cell)/self.input_cell)
                resistance = self.mainR_resist
                self.error_layer[n] = utils.movingAverage(old_value, new_value, resistance)
                
        # - Move output layer forward:
        for row in range(self.output_size):
            for el in range(self.output_size-1):
                self.output_layer[row][el] = self.output_layer[row][el+1]
            
        # - Rate the dendrites:
        # Rn = E( 1 - abs( (Pn - I0) / I0 ) )
        if self.life > self.start_predicting+1:
            for row in range(self.row_count):
                for el in range (self.row_size):
                    old_value  = self.cell_matrix_DR[row][el]
                    new_value  = 1 - abs((self.cell_matrix_P[row][el] - self.input_cell)/self.input_cell)
                    resistance = self.dRating_resist
                    Rn = utils.movingAverage(old_value, new_value, resistance)
                    # Reset Rn on bad predictions:
                    if new_value < 0.1 or Rn < 0.001:
                        Rn = 0.001
                    self.cell_matrix_DR[row][el] = Rn
        
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
                        Dn = utils.movingAverage(old_value, new_value, self.RD)
                        self.cell_matrix_D[row][el] = Dn
            # -- Update RV:
            self.RD += 1
            if self.RD > self.max_D_resist:
                self.RD = self.max_D_resist
        
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
                                                          
        # - Update the EVs:
        for row in range(self.row_count):
            for el in range(self.row_size):
                # -- EVs:
                old_value  = self.cell_matrix_EV[row][el]
                new_value  = self.cell_matrix_V[row][el]
                self.cell_matrix_EV[row][el] = utils.movingAverage(old_value, new_value, self.RV)
                
        # - Update the RV:
        self.RV += 1
        if self.RV > self.max_V_resist:
            self.RV = self.max_V_resist
        
        # - Update life:
        self.life += 1
    # END INPUT AND UPDATE
    ######################
    
    
    ##########
    # PREDICT:
    def predict(self):
        if self.life > self.start_predicting:
            # - Copy the matrices for the simulation:
            self.cell_matrix_D_copy = np.copy(self.cell_matrix_D)
            self.cell_matrix_V_copy = np.copy(self.cell_matrix_V)
            self.cell_matrix_EV_copy = np.copy(self.cell_matrix_EV)
            self.cell_matrix_DR_copy = np.copy(self.cell_matrix_DR)
        
            # SIMULATIONS:
            for n in range(self.output_size):
                # - Reconstruct next input:
                # Pn = (EI0*An - EI0*EAn + Dn)/(An - EAn) = (EI0(An - EAn) + Dn)/(An - EAn) = EI0 + Dn/(An - EAn)
                # Prediction = SUM(Pn*Rn)/SUM(Rn)
                if n == 0:
                    self.cell_matrix_P, self.output_layer[n][n] = decodeDendrites(self.cell_matrix_D_copy, 
                                                                               self.cell_matrix_V_copy, 
                                                                               self.cell_matrix_EV_copy,
                                                                               self.cell_matrix_DR_copy)
                else:
                    temp_matrix = [] # dummy matrix
                    # we only needed the first P matrix for the dendr optimization later
                    temp_matrix, self.output_layer[n][n] = decodeDendrites(self.cell_matrix_D_copy, 
                                                                        self.cell_matrix_V_copy, 
                                                                        self.cell_matrix_EV_copy,
                                                                        self.cell_matrix_DR_copy)
                                                  
                # - Move the input array back:
                for el in range(self.row_size-1):
                    self.cell_matrix_V_copy[0][-1-el] = self.cell_matrix_V_copy[0][-2-el]
                
                # - Set the A[0][0] input:
                self.cell_matrix_V_copy[0][0] = self.output_layer[n][n]
                
                # - Run connections:
                if self.pull == 1:
                    self.cell_matrix_V_copy = utils.runConnectionsPull(self.cell_matrix_V_copy,
                                                                       self.connections_list)
                else:
                    self.cell_matrix_V_copy = utils.runConnectionsPush(self.cell_matrix_V_copy,
                                                                       self.connections_list)
                
                # - Update the EVs:
                for row in range(self.row_count):
                    for el in range(self.row_size):
                        # -- EVs:
                        old_value  = self.cell_matrix_EV_copy[row][el]
                        new_value  = self.cell_matrix_V_copy[row][el]
                        self.cell_matrix_EV_copy[row][el] = utils.movingAverage(old_value, new_value, self.RV)
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
        print("- Value    change resistance:", self.RV)
        print("- Dendrite change resistance:", self.RD)
            
    # - Cell dendrites:
    def printDendrites(self):
        print()
        print("Cell dendrites:")
        for n in range(self.row_count):
            print(self.cell_matrix_D[n])
            
    # - Cell dendrite predictions:
    def printDendrPredictions(self):
        print()
        print("Cell dendrite predictions:")
        for n in range(self.row_count):
            print(self.cell_matrix_P[n])
            
    # - Cell dendrite rating:
    def printDendrRatings(self):
        print()
        print("Cell dendrite ratings:")
        for n in range(self.row_count):
            print(self.cell_matrix_DR[n]) 
            
    # END PRINTERS
    ##############
    
# END Class Predictor
#####################