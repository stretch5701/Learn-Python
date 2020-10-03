""" tic-tac-toe game based on example from automate the boring stuff.
    player enters a coordinate that matches a key in the_board.  The program
    checks that it is a valid key and that it has not been used.  After each
    turn the program checks the board to see if we have a winner."""

import sys

the_board = {'UL':'UL', 'UM':'UM', 'UR':'UR',
             'ML':'ML', 'MM':'MM', 'MR':'MR',
             'LL':'LL', 'LM':'LM', 'LR':'LR'}

players = (' X',' 0') #space for formatting


def make_rows(board):
    board_values_list = []
    rows_list = []

    board_values_list = list(board.values()) #list contains only the values

    for i in range(0,len(board_values_list),3):
        rows_list.append(board_values_list[i:i+3])

    return rows_list

def make_cols(board):
    col1, col2, col3 = [],[],[]
    values_list = list(board.values())
    
    for i in range(len(values_list)):
        if i%3 == 0:
                col1.append(values_list[i])
        elif i%3 == 1:
                col2.append(values_list[i])
        else:
                col3.append(values_list[i])

    return [col1, col2, col3]
    

def print_board(board):

    sep_line = '--+--+--\n'
    rows_list = []
    prn_str = '\n' 


    board_values_list = list(board.values()) #list contains only the values
    
    #sep into three row lists to join later with '|'
    rows_list = make_rows(board)
        
    for i in range(len(rows_list)):
        if i==0: #first row doen't need a sep_line across the top
                prn_str += '|'.join(rows_list[i])+'\n'
        else:
                prn_str += sep_line
                prn_str += '|'.join(rows_list[i])+'\n'

    print(prn_str)
    

def next_turn(play_index):
    return int(not play_index)

    
def  check_entry(entry):
    if entry in the_board.keys() and the_board[entry] not in players:
        return True
    else:
        return False

def check_board(the_board, player):
    """ checks the board to see if player has won.  Compares a list comprised
    [player, player, player] against each possible row, column or diagonal"""

    check_row = [player]*3 #[player, player, player]
    the_rows = make_rows(the_board)
    the_cols = make_cols(the_board)

    the_diags = [[the_board['UL'], the_board['MM'], the_board['LR']],
                [the_board['UR'], the_board['MM'], the_board['LL']]]

    tie = True
    #check if all the squares are taken
    for value in the_board.values():
        if value not in players:
            tie = False  # at least one spot is still open
            break
    if tie:
        print('Tie! There is no winner.')
        sys.exit()
    
    for row in the_rows:
        if row == check_row:
            return True

    for col in the_cols:
        if col == check_row:
            return True

    for diag in the_diags:
        if diag == check_row:
            return True
        
    return False


player_index = 0
player=players[player_index]


print_board(the_board)

while True:
    print('it is {}\'s turn.'.format(players[player_index]))
    correct_entry = False
    entry = input('enter board coordinates:')
    correct_entry = check_entry(entry.upper())

    while not correct_entry:
        print('That cooredinate is incorrect,')
        entry = input('enter board coordinates:')
        correct_entry =  check_entry(entry.upper())

    the_board[entry.upper()] = player
    print_board(the_board)
    
    if check_board(the_board, player):
        print('Player{} has won!'.format(player))
        break

    player_index = next_turn(player_index)
    player = players[player_index]
