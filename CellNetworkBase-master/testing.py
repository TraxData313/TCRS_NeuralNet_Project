import numpy as np
import time
from networkMod import println
from networkMod import Network

#################
# FUNCTIONS USED:
def displaySpecificConnFlowMatrix(sampleNetwork):
    println(10)
    layer = 0
    row   = 2
    col   = 2
    print "Layer :",layer
    print "Row   :",row
    print "Column:",col
    print
    print "Conn matrix:"
    print sampleNetwork.cell_grid[layer][row][col].conn_matrix
    print
    print "Flow matrix:"
    print sampleNetwork.cell_grid[layer][row][col].flow_matrix
    println(3)
    time.sleep(432)
###



# - Define the inputs
inputs = 10          # number of inputs
input_array = np.zeros(inputs)

# - Spawn a network:
sampleNetwork = Network(input_array)





#######
# LOOP:
tick = 0
while True:
    start = time.time()
    
    # - Input:
    input_array = []
    i=0
    while i < inputs:
        input_value = np.sin((tick+i)/10.)  # replace with any function/input, for example: stock prices
        input_array.append(input_value)
        i+=1    
        
    # - Operations:
    sampleNetwork.getInput(input_array)
    sampleNetwork.updateConnectionsAndFlows()
    
    # - Prints:
    sampleNetwork.printCellValues()
    #displaySpecificConnFlowMatrix(sampleNetwork)
    end   = time.time()
    print
    print "- Tick:", tick
    print "- Done!"
    print "- Loop time [ms] =", (end - start)*1000.0
    tick+=1
    time.sleep(1)
###



































