
---

# ConnectX Simulation Competition

Welcome to the ConnectX Simulation Competition repository! This project is part of a beta-version simulation competition hosted on Kaggle, where participants compete against a set of rules using Python submissions.

## Overview

This competition challenges participants to develop an AI agent capable of playing the game ConnectX. The objective is to connect a certain number of checkers in a row—horizontally, vertically, or diagonally—before the opponent does. Participants must submit a Python `.py` file that acts as an AI agent to play against other submissions.

### Features

- **Game Objective**: Achieve a specified number of checkers in a row before the opponent on a game board.
- **Submission**: Participants submit a Python `.py` file containing their AI agent's logic.
- **Evaluation**: Submissions are evaluated based on their performance against other submissions, rather than a traditional accuracy metric.
- **Rating System**: Uses a Gaussian model to estimate skill levels of submissions.

## Getting Started

To participate in this competition:

1. **Clone the Repository**: Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/connectx-competition.git
   ```

2. **Set Up Your Environment**: Ensure you have Python installed. You may also need to install the `kaggle-environments` package.

   ```bash
   pip install kaggle-environments
   ```

3. **Develop Your Agent**: Modify the `submission.py` file to implement your AI agent. Example starter code is provided to get you started.

4. **Submit Your Agent**: Once you're satisfied with your agent's performance locally, submit your `submission.py` to Kaggle through their competition interface.

## Code Structure

- **`submission.py`**: Main file where your AI agent's logic is implemented. Modify this file to improve your agent's performance.
- **`README.md`**: This file provides an overview of the competition, setup instructions, and guidelines for participating.

## Rules and Guidelines

- Your agent must return an action within 2 seconds (60 seconds on the first turn) of being invoked.
- Use only modules from the Kaggle Kernels notebook image.
- Ensure your submission does not exceed the maximum file size limit of 100 MB.

## Contributing

This competition is a beta launch, and your feedback is valuable. If you encounter issues or have suggestions for improvements, please open an issue or pull request. We appreciate your input!

## Citation

ConnectX. (2020). Kaggle. Retrieved from https://www.kaggle.com/code/namratapatel05/dqn-connect-x

---
