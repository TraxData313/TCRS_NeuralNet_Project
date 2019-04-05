import numpy as np
import random
import time



############
# FUNCTIONS:


# - println:
def println(lines):
    i=0
    while i < lines:
        print
        i+=1

        
# - createCellGrid:
def createCellGrid(layers, rows, columns):
    layer_list = []
    layer=0
    while layer < layers:
        row_list = []
        row=0
        while row < rows:
            col_list = []
            col=0
            while col < columns:
                temp_cell = Cell(layer,row,col)
                col_list.append(temp_cell)
                col+=1
            row_list.append(col_list)
            row+=1
        layer_list.append(row_list)
        layer+=1
    return layer_list
    
    
# - moveValuesBack:
def moveValuesBack(row_of_cells):
    col = 0
    while col < len(row_of_cells)-1:
        row_of_cells[-1-col].value = row_of_cells[-2-col].value
        col+=1
    return row_of_cells
    
    
# - createConnections:
def createConnections(cell_grid_3D):
    layer=0
    while layer < len(cell_grid_3D):
        row=0
        while row < len(cell_grid_3D[layer]):
            col=0
            while col < len(cell_grid_3D[layer][row]):

                cell_layer = cell_grid_3D[layer][row][col].layer
                cell_row   = cell_grid_3D[layer][row][col].row
                cell_col   = cell_grid_3D[layer][row][col].column
                min = -50 #/100
                max = 100 #/100
                
                # - Border conditions
                # -- if last layer -> no connections | checked
                if cell_layer == len(cell_grid_3D)-1:
                    conn_rows = 0
                    conn_cols = 0
                # -- if top left -> 2x2 | checked
                elif cell_row == 0 and cell_col == 0:
                    conn_rows = 2
                    conn_cols = 2
                # -- if top right -> 2x2 | checked
                elif cell_row == 0 and cell_col == len(cell_grid_3D[layer][row])-1:
                    conn_rows = 2
                    conn_cols = 2
                # -- if bottom left -> 2x2 | checked
                elif cell_row == len(cell_grid_3D[layer])-1 and cell_col == 0:
                    conn_rows = 2
                    conn_cols = 2
                # -- if bottom right -> 2x2 | checked
                elif cell_row == len(cell_grid_3D[layer])-1 and cell_col == len(cell_grid_3D[layer][row])-1:
                    conn_rows = 2
                    conn_cols = 2
                # -- if top -> row0 -> 2x3 | checked
                elif cell_row == 0:
                    conn_rows = 2
                    conn_cols = 3
                # -- if bottom -> row-1 -> 2x3 | checked
                elif cell_row == len(cell_grid_3D[layer])-1:
                    conn_rows = 2
                    conn_cols = 3
                # -- if left -> col0 -> 3x2 | checked
                elif cell_col == 0:
                    conn_rows = 3
                    conn_cols = 2
                # -- if right -> col-1 -> 3x2 | checked
                elif cell_col == len(cell_grid_3D[layer][row])-1:
                    conn_rows = 3
                    conn_cols = 2
                # -- Middle cell -> 3x3
                else:
                    conn_rows = 3
                    conn_cols = 3
                # - Create the connection list:
                conn_matrix = []
                flow_matrix = []
                r=0
                while r < conn_rows:
                    temp_conn_row = []
                    temp_flow_row = []
                    c=0
                    while c < conn_cols:
                        tepm_weight = random.randint(min,max)/100.
                        temp_flow   = 0.
                        temp_conn_row.append(tepm_weight)
                        temp_flow_row.append(temp_flow)
                        c+=1
                    conn_matrix.append(temp_conn_row)
                    flow_matrix.append(temp_flow_row)
                    r+=1
                # - Add the matrices to the cell:
                cell_grid_3D[layer][row][col].conn_matrix = conn_matrix
                cell_grid_3D[layer][row][col].flow_matrix = flow_matrix
                    
                col+=1
            row+=1
        layer+=1
    return cell_grid_3D
### END FUNCIONS
    
    
    
    
    
    
    
    
    
#############
# Class CELL:
class Cell:
    def __init__(self,layer,row,column):
        self.value     = 0.
        self.value_old = 0.
        self.value_der = 0.
        self.layer  = layer
        self.row    = row
        self.column = column
        self.conn_matrix = []
        self.flow_matrix = []
    
    def __repr__(self):
        return "{}".format(self.value)
### END Class CELL
    
    

    
    
    
    
    
    
################
# Class NETWORK:
class Network:
    # INITIATORS:
    
    def __init__(self, input_array):
        # - Parameters:
        self.life = 0
        self.inputs_count = len(input_array)                #rows
        self.input_size   = self.inputs_count               #columns
        self.arrays_count = self.input_size  #layers   = columns for now
        # - Objects:
        self.cell_grid = []
        # - Create the 3D cell grid:
        self.cell_grid = createCellGrid(self.arrays_count, self.inputs_count, self.input_size)
        # - Create connections for the cells depending on their positions:
        self.cell_grid = createConnections(self.cell_grid)
        
    # END INITIATORS

    
    
    # OPERATORS:
    
    # - getInput:
    def getInput(self, input_array):
        row=0
        while row < self.inputs_count:
            # - Move values back in time:
            self.cell_grid[0][row] = moveValuesBack(self.cell_grid[0][row])
            # - Get input:
            self.cell_grid[0][row][0].value = input_array[row]
            row+=1
            
            
    # - updateConnectionsAndFlows:
    def updateConnectionsAndFlows(self):
        # - Set the old values:
        layer=0
        while layer < self.arrays_count:
            row=0
            while row < self.inputs_count:
                col=0
                while col < self.input_size:
                    self.cell_grid[layer][row][col].value_old = self.cell_grid[layer][row][col].value
                    col+=1
                row+=1
            layer+=1
       
        
        
        
        
        # - Reset the last layer:
        row=0
        while row < len(self.cell_grid[-1]):
            col=0
            while col < len(self.cell_grid[-1][row]):
                self.cell_grid[-1][row][col].value = 0
                col+=1
            row+=1
        # -
        layer = self.arrays_count-2
        while layer > -1:
            row=0
            while row < len(self.cell_grid[layer]):
                col=0
                while col < len(self.cell_grid[layer][row]):
                    cell_layer = self.cell_grid[layer][row][col].layer
                    cell_row   = self.cell_grid[layer][row][col].row
                    cell_col   = self.cell_grid[layer][row][col].column
                    # - Border condition decoders:
                    # -- if top left (2x2):
                    if cell_row == 0 and cell_col == 0:
                        r_size = 2
                        c_size = 2
                        rr     = 0
                        cc     = 0
                    # -- if top right (2x2):
                    elif cell_row == 0 and cell_col == len(self.cell_grid[layer][row])-1:
                        r_size = 2
                        c_size = 2
                        rr     = 0
                        cc     = -1
                    # -- if bottom left (2x2):
                    elif cell_row == len(self.cell_grid[layer])-1 and cell_col == 0:
                        r_size = 2
                        c_size = 2
                        rr     = -1
                        cc     = 0
                    # -- if bottom right (2x2):
                    elif cell_row == len(self.cell_grid[layer])-1 and cell_col == len(self.cell_grid[layer][row])-1:
                        r_size = 2
                        c_size = 2
                        rr     = -1
                        cc     = -1
                    # -- if top (2x3):
                    elif cell_row == 0:
                        r_size = 2
                        c_size = 3
                        rr     = 0
                        cc     = -1
                    # -- if bottom (2x3):
                    elif cell_row == len(self.cell_grid[layer])-1:
                        r_size = 2
                        c_size = 3
                        rr     = -1
                        cc     = -1
                    # -- if left (3x2):
                    elif cell_col == 0:
                        r_size = 3
                        c_size = 2
                        rr     = -1
                        cc     = 0
                    # -- if right (3x2):
                    elif cell_col == len(self.cell_grid[layer][row])-1:
                        r_size = 3
                        c_size = 2
                        rr     = -1
                        cc     = -1
                    # -- Middle cell (3x3):
                    else:
                        r_size = 3
                        c_size = 3
                        rr     = -1
                        cc     = -1
                    # -- Recover the matrices:
                    conn_matrix = self.cell_grid[layer][row][col].conn_matrix
                    flow_matrix = self.cell_grid[layer][row][col].flow_matrix
                    # -- Recover the source value:
                    source      = self.cell_grid[layer][row][col].value
                    # -- Loop the cell matrices:
                    r = 0
                    while r < r_size: #r size
                        c = 0
                        while c < c_size: #c size
                            # --- Recover the target value based on the border conditions*:
                            target = self.cell_grid[layer+1][row+r+rr][col+c+cc].value
                            # --- Calculate the 
                            target = source*conn_matrix[r][c]
                            # --- Add the new value to the target:
                            self.cell_grid[layer+1][row+r+rr][col+c+cc].value += target
                            # --- Update the flow:
                            flow_matrix[r][c] += source*conn_matrix[r][c]
                            # --- Apply RELU:
                            if self.cell_grid[layer+1][row+r+rr][col+c+cc].value < 0:
                                self.cell_grid[layer+1][row+r+rr][col+c+cc].value = 0
                            c+=1
                        r+=1
                    # -- Reset the source:
                    if layer > 0:
                        self.cell_grid[layer][row][col].value = 0
                    col+=1
                row+=1
            layer=layer-1
        # - Calculate the ders:
        layer=0
        while layer < self.arrays_count:
            row=0
            while row < self.inputs_count:
                col=0
                while col < self.input_size:
                    self.cell_grid[layer][row][col].value_der = self.cell_grid[layer][row][col].value - self.cell_grid[layer][row][col].value_old
                    col+=1
                row+=1
            layer+=1
            
    # END OPERATORS
    
    

    # PRINTERS
    
    # - __repr__:
    def __repr__(self):
        return "Network life: {}".format(self.life)
        
        
    # - printCellValues:
    def printCellValues(self):
        print
        print "Cell values:"
        print
        layer=0
        while layer < self.arrays_count:
            print
            row=0
            print "- Layer", layer
            while row < self.inputs_count:
                print self.cell_grid[layer][row]
                row+=1
            layer+=1

    # END PRINTERS
### END Class NETWORK








































'''
NOTES:
- Minimum network size = 3x3x3 due to cell conn&flow matrix border conditions. 
-- Check function createConnections for more details


*Connection matrices Border conditions:
Cell : C[layer][row][col]
- Top left cell (2x2):
C[layer+1][row][col] targeted by w[r=0][c=0]
C[layer+1][row+r][col+c] = C[layer][row][col]*w[r][c]
- Top right cell (2x2):
C[layer+1][row][col] targeted by w[r=0][c=1]
C[layer+1][row+r][col+c-1] = C[layer][row][col]*w[r][c]
- Bottom left cell (2x2):
C[layer+1][row][col] targeted by w[r=1][c=0]
C[layer+1][row+r-1][col+c] = C[layer][row][col]*w[r][c]
- Bottom right cell (2x2):
C[layer+1][row][col] targeted by w[r=1][c=1]
C[layer+1][row+r-1][col+c-1] = C[layer][row][col]*w[r][c]
- Top cell (2x3):
C[layer+1][row][col] targeted by w[r=0][c=1]
C[layer+1][row+r][col+c-1] = C[layer][row][col]*w[r][c]
- Bottom cell (2x3):
C[layer+1][row][col] targeted by w[r=1][c=1]
C[layer+1][row+r-1][col+c-1] = C[layer][row][col]*w[r][c]
- Left cell (3x2):
C[layer+1][row][col] targeted by w[r=1][c=0]
C[layer+1][row+r-1][col+c] = C[layer][row][col]*w[r][c]
- Right cell (3x2):
C[layer+1][row][col] targeted by w[r=1][c=1]
C[layer+1][row+r-1][col+c-1] = C[layer][row][col]*w[r][c]
- Standart cell (3x3):
C[layer+1][row][col] targeted by w[r=1][c=1]
C[layer+1][row+r-1][col+c-1] = C[layer][row][col]*w[r][c]
'''


























