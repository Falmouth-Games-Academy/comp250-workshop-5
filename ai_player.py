import random


def choose_move(board):
    """ Takes a game board, and returns a move to play
    """
    
    available_moves = board.get_moves()
    return random.choice(available_moves)
