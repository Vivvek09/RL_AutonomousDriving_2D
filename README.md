# CarRacing-v2 with PPO Reinforcement Learning

This project implements a reinforcement learning (RL) agent using the Proximal Policy Optimization (PPO) algorithm to master the **CarRacing-v2** environment from the Gymnasium library. The project aims to explore the intersection of computer vision, reinforcement learning, and control systems, providing an entry point for anyone interested in these domains.

## Project Overview

CarRacing-v2 is a top-down 2D racing environment, providing a simplified yet challenging control task where the goal is to maximize the agent's performance by learning from raw pixel data. This environment serves as an ideal testbed for experimenting with deep reinforcement learning algorithms like PPO, as it requires the agent to make continuous decisions in a dynamic environment.

### Action Space

- **Continuous**: The action space is represented as a Box with 3 continuous actions:
  1. **Steering**: -1 (full left) to +1 (full right)
  2. **Gas**: 0 (no gas) to 1 (full throttle)
  3. **Brake**: 0 (no brake) to 1 (full brake)

### Observation Space

- The observation space is a 96x96 RGB image, representing the car and the racetrack.

### Reward System

- The reward system incentivizes the agent to complete the track as efficiently as possible, with penalties for each frame and rewards for every tile visited.

## Project

The project includes a Streamlit application that showcases the performance of the trained model. You can view the Streamlit app by following this link:

## Future Work

While this project focuses on a 2D environment, I am enthusiastic about expanding this work into 3D virtual environments. This transition will involve more complex state representations and control dynamics, offering richer challenges for reinforcement learning algorithms. I am particularly interested in applying these techniques to real-world scenarios, such as autonomous driving and robotic control.
