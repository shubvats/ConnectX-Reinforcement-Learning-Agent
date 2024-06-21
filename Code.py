import numpy as np
import random

# Gets board at next step if agent drops piece in selected column
def drop_piece(grid, col, piece, config):
    """
    Returns the board configuration after dropping a piece in the specified column.
    
    Args:
    - grid (numpy array): Current game board as a 2D numpy array.
    - col (int): Column where the piece will be dropped.
    - piece (int): Piece value (1 or 2) representing the agent's or opponent's piece.
    - config (object): Configuration object containing game settings.
    
    Returns:
    - numpy array: Updated game board after dropping the piece.
    """
    next_grid = grid.copy()
    for row in range(config.rows-1, -1, -1):
        if next_grid[row][col] == 0:
            break
    next_grid[row][col] = piece
    return next_grid

# Returns True if dropping piece in column results in game win
def check_winning_move(obs, config, col, piece):
    """
    Checks if dropping a piece in a column results in a win for the specified piece.
    
    Args:
    - obs (object): Observation object containing the current board state and mark of the agent.
    - config (object): Configuration object containing game settings.
    - col (int): Column to check for a winning move.
    - piece (int): Piece value (1 or 2) representing the agent's or opponent's piece.
    
    Returns:
    - bool: True if dropping a piece in the column results in a win, False otherwise.
    """
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    next_grid = drop_piece(grid, col, piece, config)
    
    # Check for win in horizontal, vertical, and diagonal directions
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[row,col:col+config.inarow])
            if window.count(piece) == config.inarow:
                return True
    
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(next_grid[row:row+config.inarow,col])
            if window.count(piece) == config.inarow:
                return True
    
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row+config.inarow), range(col, col+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    
    return False

# Agent that selects a winning move or random move
def agent_q1(obs, config):
    """
    Agent that selects a winning move if available, otherwise selects a random move.
    
    Args:
    - obs (object): Observation object containing the current board state and mark of the agent.
    - config (object): Configuration object containing game settings.
    
    Returns:
    - int: Selected column where the agent decides to drop its piece.
    """
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    
    # Check for winning move
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    
    # If no winning move, choose a random move
    return random.choice(valid_moves)

# Agent that blocks opponent's winning moves and selects a winning move
def agent_q2(obs, config):
    """
    Agent that selects a winning move if available, blocks opponent's winning move if necessary,
    otherwise selects a random move.
    
    Args:
    - obs (object): Observation object containing the current board state and mark of the agent.
    - config (object): Configuration object containing game settings.
    
    Returns:
    - int: Selected column where the agent decides to drop its piece.
    """
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    
    # Check for winning move
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    
    # Check for opponent's winning move and block it
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark % 2 + 1):
            return col
    
    # If neither winning nor blocking move is available, choose a random move
    return random.choice(valid_moves)
