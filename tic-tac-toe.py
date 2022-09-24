"""
Tic-Tac-Toe: is a game in which two players seek in alternate turns to complete a row, a column,
or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
Author: Sister Ferreira
"""

def main():
    players = game_introduction()    
    position = ["1","2","3","4","5","6","7","8","9"] 
    turn = 0
    move = [position, 0]
    for x in position:
        move = play(players[turn], move[0], turn)
        status = verify_status(position, turn, move[1])
        if status == True : 
            final_message(players[turn], position)
            break
        if turn == 0 : turn = turn + 1 
        else : turn = 0
    if status == False:
        print(f"\n {position[0]} │ {position[1]} │ {position[2]} \n───┼───┼───\n {position[3]} │ {position[4]} │ {position[5]} \n───┼───┼───\n {position[6]} │ {position[7]} │ {position[8]}")
        print("\nAnyone's won! :) Good game. Thanks for playing!")

def game_introduction():
    """welcome to the game and assign the players"""
    
    print("\n================ Welcome to Tic-Tac-Toe game ========================\nTic-Tac-Toe is a game in which two players seek in alternate\nturns to complete a row, a column, or a diagonal with either\nthree x's or three o's drawn in the spaces of a grid of nine squares.\nThe first player to get three of their marks in a row is the winner.\n=====================================================================\n")
    
    players = ["",""]
    
    players[0] = input("Enter the name of the player one(x): ")
    players[1] = input("Enter the name of the player two(0): ")
    
    print(f"\nWelcome,{players[0]} and {players[1]}! Let's go to play!")
    
    return players
    
def play(player, position, turn):
    """Movement record"""

    print(f"\n {position[0]} │ {position[1]} │ {position[2]} \n───┼───┼───\n {position[3]} │ {position[4]} │ {position[5]} \n───┼───┼───\n {position[6]} │ {position[7]} │ {position[8]}")
    option = input(f"\n{player}, please choose an empty square (1-9): ")
    
    if turn == 0 : figure = "X"
    else : figure = "0"
    
    while position[int(option)-1] == figure:
       option = input(f"\n{player}, Your option is invalid! Please choose an empty square. (1-9): ")
    
    validate = False
    while validate == False:
        try:
            position[position.index(option)] = figure
            validate = True
        except:
            option = input(f"\n{player}, Your option is invalid! Please choose an empty square. (1-9): ")
            validate = False
    
    return [position, option] 

def verify_status(position, turn, option): 
    """verify if there is a winner"""
    if turn == 0 : figure = "X"
    else : figure = "0"
    status = False
    
    if option == "1" :
        if position[1] == figure and position[2] == figure: status = True
        if position[3] == figure and position[6] == figure: status = True
        if position[4] == figure and position[8] == figure: status = True
        
    if option == "2" :
        if position[0] == figure and position[2] == figure: status = True
        if position[4] == figure and position[7] == figure: status = True
        
    if option == "3" :
        if position[1] == figure and position[0] == figure: status = True
        if position[5] == figure and position[8] == figure: status = True
        if position[4] == figure and position[6] == figure: status = True
        
    if option == "4" :
        if position[0] == figure and position[6] == figure: status = True
        if position[4] == figure and position[5] == figure: status = True
        
    if option == "5" :
        if position[0] == figure and position[8] == figure: status = True
        if position[2] == figure and position[6] == figure: status = True
        if position[1] == figure and position[7] == figure: status = True
        
    if option == "6" :
        if position[2] == figure and position[8] == figure: status = True
        if position[3] == figure and position[4] == figure: status = True
        
    if option == "7" :
        if position[0] == figure and position[3] == figure: status = True
        if position[2] == figure and position[4] == figure: status = True
        if position[7] == figure and position[8] == figure: status = True
        
    if option == "8" :
        if position[1] == figure and position[4] == figure: status = True
        if position[6] == figure and position[8] == figure: status = True
        
    if option == "9" :
        if position[0] == figure and position[4] == figure: status = True
        if position[2] == figure and position[5] == figure: status = True
        if position[6] == figure and position[7] == figure: status = True
        
        
    return status

def final_message(player, position): 
    """when the game end, print a message with the result"""

    print(f"\n {position[0]} │ {position[1]} │ {position[2]} \n───┼───┼───\n {position[3]} │ {position[4]} │ {position[5]} \n───┼───┼───\n {position[6]} │ {position[7]} │ {position[8]}")
    print(f"\n {player}, you win! Good game. Thanks for playing!")
    
if __name__ == "__main__":
    main()