import numpy as np
import random
import time
import copy
from simplePermutator import SimplePermutator
from utils import println


# Controls:
controlsFile      = 'tictactoe_controls.txt'
controlsList      = []
controlsList      = open(controlsFile, 'r').readlines()
commentary        = int(controlsList[1]) # 1=on / 0=off

# Parameters:
number_of_players = 2
hidden_size       = 10
hidden_count      = 7
#dendrite_resist   = 10
think_before_move = 1
reset_cell_values = 0
sleep_time        = 0.5


# Variables:
ave_g_played      = 0
g_restist         = 150

# Fixed parameters:
input_size        = 18
output_size       = 9

# Create the networks:
list_of_networks  = []
n = 0
while n < number_of_players:
    sampleNetwork = SimplePermutator(input_size, 
                            hidden_size,
                            hidden_count,
                            output_size)
    list_of_networks.append(sampleNetwork)
    n+=1



###
bot = 0
###


############
# FUNCTIONS:

def printTable(P1,P2,Free):
    print()
    Table = []
    n=0
    while n < 9:
        if Free[n] == 0:
            Table.append('*')
        elif P1[n] == 1:
            Table.append('X')
        elif P2[n] == 1:
            Table.append('O')
        n+=1
    print( "---------")
    print( "|", Table[0], Table[1], Table[2], "|")
    print( "|", Table[3], Table[4], Table[5], "|")
    print( "|", Table[6], Table[7], Table[8], "|")
    print( "---------"  )

# END FUNCTIONS
###############






# pick two ordered players:
player_1 = list_of_networks[0]
player_2 = list_of_networks[1]


#######
# LOOP:
tick = 0
while True:


    #println(10)

    # - Check the controls:
    
    controlsList    = []
    controlsList    = open(controlsFile, 'r').readlines()
    commentary      = int(controlsList[1]) # 1=on / 0=off
    bot             = int(controlsList[2]) # 1=on / 0=off
    '''
    if tick > 1000:
        commentary = 1
    '''
    
    
    if commentary == 1:
        print( "STARTING A NEW GAME NOW!!!")
    
    # pick two random players:
    '''
    # - player 1:
    player   = random.randint(0,number_of_players-1)
    player_1 = list_of_networks[player]
    list_of_networks.pop(player)
    # - player 2:
    player   = random.randint(0,number_of_players-2)
    player_2 = list_of_networks[player]
    list_of_networks.pop(player)
    if commentary == 1:
        print "Player 1", player, player_1
        print "Player 2", player, player_2
    '''
        

    
        
    
    #######
    # GAME:
    P1   = [False] * 9
    P2   = [False] * 9
    Free = [False] * 9
    game_active = 1 # 1 active, 2 finished
    moves = 0.
    player_to_move = 1 # 1 or 2 
    feedbackCell = 0
    while game_active == 1:

        # - Get the input_move prepared:
        input_move = []
        
        # - Player 1:
        if player_to_move == 1:
            input_move = []
            el = 0
            while el < 9:
                input_move.append(P1[el])
                el+=1
            el = 0
            while el < 9:
                input_move.append(Free[el])
                el+=1
            n = 0
            while n < think_before_move:
                player_1.get_input(input_move)
                n+=1
                
            # - Get the output:
            output_place = player_1.returnOutputPlace()
            
            # - Check if the place decided is free
            place_to_mark           = output_place
            if Free[place_to_mark] == 0:
                Free[place_to_mark] = 1
                P1[place_to_mark]   = 1
                # - Check for win condition:
                if P1[0] == 1 and P1[1] == 1 and P1[2] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[3] == 1 and P1[4] == 1 and P1[5] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[6] == 1 and P1[7] == 1 and P1[8] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[0] == 1 and P1[3] == 1 and P1[6] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[1] == 1 and P1[4] == 1 and P1[7] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[2] == 1 and P1[5] == 1 and P1[8] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[0] == 1 and P1[4] == 1 and P1[8] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                elif P1[2] == 1 and P1[4] == 1 and P1[6] == 1:
                    game_active = 0
                    feedback    = 2
                    player_1.rewardAndUpdate(feedback)
                    feedback    = -1
                    player_2.rewardAndUpdate(feedback)
                    if commentary == 1:
                        printTable(P1,P2,Free)
                        time.sleep(sleep_time)
                        print("Player 1 WON !!!")
                else:
                    feedback = moves*0.3 
                    player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
            else:
                # -- NOT free place feedback:
                feedback = - 1 + moves*0.2
                player_1.rewardAndUpdate(feedback)
                game_active = 0
            player_to_move = 2
            
            
            
        if player_to_move == 2 and bot == 0 and game_active == 1:
            # - Player 2 = Human inut:
            print("input_move your move as O:")
            output_place = input("Move? ")
            output_place = int(output_place)
            player_to_move = 1
            
        
        elif bot == 1:
            # - Player 2:
            input_move = []
            if player_to_move == 2 and game_active == 1:
                el = 0
                while el < 9:
                    input_move.append(P2[el])
                    el+=1
                el = 0
                while el < 9:
                    input_move.append(Free[el])
                    el+=1
                n = 0
                while n < think_before_move:
                    player_2.getInputAndPropagate(input_move)
                    n+=1
                # - Get the output:
                output_place = player_2.returnOutputPlace()
                
        # - Check if the place decided is free
        place_to_mark           = output_place
        if Free[place_to_mark] == 0:
            Free[place_to_mark] = 1
            P2[place_to_mark]   = 1
            # - Check for win condition:
            if P2[0] == 1 and P2[1] == 1 and P2[2] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[3] == 1 and P2[4] == 1 and P2[5] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[6] == 1 and P2[7] == 1 and P2[8] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[0] == 1 and P2[3] == 1 and P2[6] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[1] == 1 and P2[4] == 1 and P2[7] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[2] == 1 and P2[5] == 1 and P2[8] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[0] == 1 and P2[4] == 1 and P2[8] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            elif P2[2] == 1 and P2[4] == 1 and P2[6] == 1:
                game_active = 0
                if bot == 1:
                    feedback    = 2
                    player_2.rewardAndUpdate(feedback)
                feedback    = -1
                player_1.rewardAndUpdate(feedback)
                if commentary == 1:
                    printTable(P1,P2,Free)
                    time.sleep(sleep_time)
                    print("Player 2 WON !!!")
            else:
                if bot == 1:
                    feedback = moves*0.3 
                    player_2.rewardAndUpdate(feedback)
            if commentary == 1:
                printTable(P1,P2,Free)
                time.sleep(sleep_time)
        else:
            # -- NOT free place feedback:
            if bot == 1:
                feedback = - 0.8 + moves*0.2
                player_2.rewardAndUpdate(feedback)
            game_active = 0
            
        player_to_move = 1
                    
            
        # Moves +1:
        moves += 1
        ave_g_played = (ave_g_played*g_restist + moves)/(g_restist+1)

        
    
        

    # - Reset cell values:
    if reset_cell_values == 1:
        player_1.resetCells()
        player_2.resetCells()
        
    '''
    # - Return the players to the list:
    list_of_networks.append(player_1)
    list_of_networks.append(player_2)
    '''
        
           
    # END GAME
    ##########


            
            
    # ending loop  
    if tick%50 == 0:
        print( "Tick: ", tick)
        print( "Games:", ave_g_played)
    if commentary == 1:
        time.sleep(1)
    tick+=1
# pass 
    








































