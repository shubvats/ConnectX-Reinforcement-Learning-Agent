def my_agent(obs, config):
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)
