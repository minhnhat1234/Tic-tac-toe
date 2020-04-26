"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0
    for i in range(len(board)):
        for value in board[i]:
            if value == X:
                x_num += 1
            elif value == O:
                o_num += 1
    return O if x_num > o_num else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []
    for i in range(len(board)):
        for j, value in enumerate(board[i]):
            if value == EMPTY:
                action_list.append((i,j))
    return set(action_list)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_new = copy.deepcopy(board)
    player_turn = player(board)
    board_new[action[0]][action[1]] = player_turn
    return board_new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(len(board)):
        if all([board[x][j] == board[x][j+1] for j in range((len(board) - 1))]):
            return board[x][0]
        if all([board[i][x] == board[i+1][x] for i in range((len(board) - 1))]):
            return board[0][x]
    if all([board[x][x] == board[x+1][x+1] for x in range((len(board) - 1))]):
        return board[0][0]
    if all([board[x][len(board) - 1 - x] == board[x+1][len(board) - 2 - x] for x in range((len(board) - 1))]):
        return board[0][len(board) - 1]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    action_set = actions(board)
    return any([len(action_set) == 0, winner(board)])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if terminal(board):
        if win == X:
            return 1
        elif win == O:
            return -1
        elif win == False:
            return 0
    else:
        return False

def return_value(board):
    action_set = actions(board)
    if not utility(board):
        value_list = []
        for x in action_set:
            board_new = result(board,x)
            value_list.append(return_value(board_new))
        if len(value_list) == 0:
            return 0
        if player(board) == X:
            max_value = max(value_list)
            return max_value
        if player(board) == O:
            min_value = min(value_list)
            return min_value
    else:
        return utility(board)

            
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    action_set = actions(board)
    action_dict = {}
    for x in action_set:
        value = return_value(result(board,x))
        action_dict[value] = x
    if len(action_dict) == 1:
        return action_dict[list(action_dict.keys())[0]]
    if player(board) == X:
        return action_dict[max([i for i in action_dict.keys()])]
    elif player(board) == O:
        return action_dict[min([i for i in action_dict.keys()])]
        

