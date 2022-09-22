
def main():
    players = game_introduction()
    

def game_introduction():
    ###
    # welcome to the game and assign the players
    ###
    
    print("\n================ Welcome to Tic-Tac-Toe game ========================\nTic-Tac-Toe is a game in which two players seek in alternate\nturns to complete a row, a column, or a diagonal with either\nthree x's or three o's drawn in the spaces of a grid of nine squares.\nThe first player to get three of their marks in a row is the winner.\n=====================================================================\n")
    
    players = ["",""]
    
    players[0] = input("Enter the name of the player one: ")
    players[1] = input("Enter the name of the player two: ")
    
    return players
    
def play(player):
    ### 
    # movement record
    # ###
    
    return 

def verify_status(position): 
    ###
    # verify if there is a winner
    # ###
    
    return

def final_message(result): 
   ### 
   # when the game end, print a message with the result
   # ### 
    
    return
    
main()