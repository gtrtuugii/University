# Task 1
def create_board():
    """ CREATE BOARD"""
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board

# Task 2

def cell(board,row,column):
    """ ACCESS BOARD"""
    return board[row][column]
# Task 3

def row_information(board, row_number):
    """ GET INFO ROW NUMBER"""
    return board[row_number]

def column_information(board,col_number):
    col_list = [board[0][col_number], board[1][col_number], board[2][col_number]]
    return col_list
# Global Constants
TOP_LEFT_TO_BOTTOM_RIGHT = 0
TOP_RIGHT_TO_BOTTOM_LEFT = 1

# Task 4
def diagonal_information(board, selected_diogonal):
    """ CHECK DIA INFO"""
    if selected_diogonal == 0:
        diogonal_list = [cell(board, 0, 0), cell(board, 1, 1), cell(board, 2, 2)]
    elif selected_diogonal == 1:
        diogonal_list = [cell(board, 0, 2), cell(board, 1, 1), cell(board, 2, 0)]
    return diogonal_list
# Task 5
def empty_cells(board):
    """FIND EMPTY CELLS"""
    empty_list = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                empty_list.append((row, column))
    return empty_list
# Task 6
def line_winner(line):
    """ LINE WINNER"""
    if line[0] != " " and line[0] == line[1] and line[1] == line[2]:
        return line[0]
   
    return None
# Task 7
def winner(board):
    """ CHECK IF WINNER"""
    for count in range(3):
        line_row = row_information(board, count)
        line_row_winner = line_winner(line_row)
        line_col = column_information(board, count)
        line_col_winner = line_winner(line_col)
        line_dio_0 = diagonal_information(board, 0)
        line_dio_0_winner = line_winner(line_dio_0)
        line_dio_1 = diagonal_information(board, 1)
        line_dio_1_winner = line_winner(line_dio_1)
        if line_row_winner != None:
            return line_row[0]
        elif line_col_winner != None:
            return line_col[0]
        elif line_dio_0_winner != None:
            return line_dio_0[0]
        elif line_dio_1_winner != None:
            return line_dio_1[0]
    return None
# Task 8
def game_over(board):
    """ GAME OVER?"""
    winner_func = winner(board)
    empty_cell = empty_cells(board)
    if winner_func != None or not empty_cell:
        return True
    
    return False
# Task 9
def game_result(board):
    """ GAME RESULT, WINNER"""
    winner_res = winner(board)
    if winner_res != None:
        result = 'Won by ' + winner_res
        return result

    if game_over(board):
        if winner(board) == None:
            return 'Draw'
    return None



# Task 10
def make_human_move(current_player, board):
    """ HUMAN MOVE"""
    print("{}'s move".format(current_player))
    empty_cell = empty_cells(board)
    if not empty_cell:
        return None
    while True:
        inp = input('Enter row and column [0 - 2]:')
        input_list = inp.split()
        row, column = int(input_list[0]), int(input_list[1])
        if (0 <= column < 3 and 0 <= row < 3) and (row, column) in empty_cell:
            board[row] [column] = current_player
            break
        else:
            print('Illegal move. Try again.')
import random
# Task 11
def make_computer_move(current_player, board):
    empty_cell = empty_cells(board)
    if len(empty_cell) == 0:
        return None
    index = random.randint(0,len(empty_cell)-1)
    row, column = empty_cell[index][0], empty_cell[index][1]
    board[row][column] = current_player
    
def play_one_turn(board, current_player, human_player):
    """ PLAYER OR CPU"""
    if current_player == human_player:
        make_human_move(current_player, board)
    else:
        make_computer_move(current_player, board)
# Task 12
def other_player(player):
    """ SHAPE OF OTHER PLAYER"""
    if player == 'X':
        return 'O'

    return 'X'
# Task 13
def get_O_or_X():
    """ SELECT SHAPE"""
    boolean = True
    while boolean:
        get = input('Would you like to play O or X? ')
        if get == 'O':
            return 'O'
        elif get == 'X':
            return 'X'
# Task 14
def play_game(human_player, board):
    current_player = human_player
    while True:
        print(board[0],'\n',board[1],'\n',board[2])
        play_one_turn(board,current_player,human_player)
        current_player = other_player(current_player)
        play_one_turn(board,current_player,human_player)
        result = game_result(board)
        if result != None:
            print(result)

# Task 15
def main():
    board = create_board()
    human_player = get_O_or_X()
    try:
        play_game(human_player,board)
        game_result(board)
        winner(board)
        line_winner(line)
    except ValueError:
            print("The program has encountered an error and needs to die. Bye.")    