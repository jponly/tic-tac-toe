def display_board(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

test_board = [' ']*10
display_board(test_board)

def player_input():
    marker = ''

    #keep asking player 1 to choose x or o

    while not (marker != 'x' and marker != 'o'):
        marker = input('Player 1, choose x or o: ').upper()

    #assign player 2 the opposite marker
    if marker == 'x':
        return ('x','o')
    else:
            return('o','x')

   



 
