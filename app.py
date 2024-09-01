import streamlit as st
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import os
import numpy as np

# Load the trained PPO model
model_path = 'PPO_Driving_Model.zip'
model = PPO.load(model_path)

# Set up the environment
environment_name = 'CarRacing-v2'
env = gym.make(environment_name, render_mode="rgb_array")  # Use rgb_array for Streamlit
env = DummyVecEnv([lambda: env])

st.title("Car Racing with PPO Model")

# Start an episode
if st.button('Start Episode'):
    state = env.reset()
    done = False
    score = 0

    stframe = st.empty()
    while not done:
        action, _ = model.predict(state)
        observation, reward, done, info = env.step(action)
        score += reward

        # Render the environment and display in Streamlit
        image = env.render(mode='rgb_array')
        stframe.image(image, caption=f'Score: {score}', use_column_width=True)

    st.write(f"Episode finished with score: {score}")

# Close the environment after use
env.close()
