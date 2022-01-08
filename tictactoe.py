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
    xcount=0
    ocount=0
    for i in range(3):
        for j in range (3):
            if board[i][j]==X:
                xcount+=1
            if board[i][j]==O:
                ocount+=1            
    if xcount<=ocount: return X
    else: return O
    """
    Returns player who has the next turn on a board.
    """


def actions(board):                     #actions in list
    L=[]
    for i in range (3):
        for j in range(3):
            if board[i][j]==None:
                L.append((i,j))
    return L        
    """
    Returns set of all possible actions (i, j) available on the board.
    """


def result(board, action):
    result=copy.deepcopy(board)
    if action!=None:
        if board[action[0]][action[1]]==EMPTY:
            result[action[0]][action[1]]=player(board)
    return result
    """
    Returns the board that results from making move (i, j) on the board.
    """


def winner(board):
    for i in range (len(board)):
        if board[0][i]==board[1][i]==board[2][i]!=EMPTY: return board[0][i]
    for j in range (len(board[0])):
        if board[j][0]==board[j][1]==board[j][2]!=EMPTY: return board[j][0]
    if board[0][0]==board[1][1]==board[2][2]!=EMPTY :
        return board[0][0]
    if board[2][0]==board[1][1]==board[0][2]!=EMPTY:
        return board[1][1]
    return None
    """
    Returns the winner of the game, if there is one.
    """


def terminal(board):
    if (winner(board)==X) or (winner(board)==O):
        return True
    a=True
    for i in range (3):
        for j in range (3):
            if board[i][j]==None:
                a=False
    return a
    """
    Returns True if game is over, False otherwise.
    """


def utility(board):
    if terminal(board):
        if winner(board)==X: return 1
        elif winner(board)==O:return -1
        else: return 0
    else: return None

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    if player(board)==X:
        v,act=max_v(board)
    if player(board)==O:
        v,act=min_v(board)
    return act

def max_v(board):
    act=None
    if terminal(board): return utility(board), act
    a=actions(board)
    v=-math.inf 
    for i in a:
        v1,ac=min_v(result(board,i))
        if v1>v:
            v=v1
            act=i
        if v == 1 : return (v,act)
    return (v,act)

def min_v(board):
    act=None
    if terminal(board): return utility(board), act
    a=actions(board)
    v=math.inf 
    for i in a:
        v1,ac=max_v(result(board,i))
        if v1<v:
            v=v1
            act=i
        if v == -1 : return (v,act)
    return (v,act)