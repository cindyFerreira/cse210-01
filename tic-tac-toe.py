
def main():
    players = game_introduction()    
    position = ["1","2","3","4","5","6","7","8","9"]    
    play(players[0],position, 0)
    

def game_introduction():
    """welcome to the game and assign the players"""
    
    print("\n================ Welcome to Tic-Tac-Toe game ========================\nTic-Tac-Toe is a game in which two players seek in alternate\nturns to complete a row, a column, or a diagonal with either\nthree x's or three o's drawn in the spaces of a grid of nine squares.\nThe first player to get three of their marks in a row is the winner.\n=====================================================================\n")
    
    players = ["",""]
    
    players[0] = input("Enter the name of the player one(x): ")
    players[1] = input("Enter the name of the player two(o): ")
    
    print(f"\nWelcome,{players[0]} and {players[1]}! Lets go to play!")
    
    return players
    
def play(player, position, turn):
    """Movement record"""

    print(f"\n {position[0]} │ {position[1]} │ {position[2]} \n───┼───┼───\n {position[3]} │ {position[4]} │ {position[5]} \n───┼───┼───\n {position[6]} │ {position[7]} │ {position[8]}")
    option = input(f"\n{player},please choose a empty square: ")
    
    if turn == 0 : figure = "X"
    else : figure = "O"
    
    position[position.index(option)] = figure
    
    return position 

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