import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

# Define NetworkDefence Class
class NetworkEnv(gym.Env):
    def __init__(self, Dataframe : pd.DataFrame = None, max_steps : int = 500):
        super(NetworkEnv, self).__init__()
        self.Dataframe = Dataframe
        self.shape = Dataframe.shape
        # Action Space : 0 - Allow | 1 - Deny
        self.action_space = spaces.Discrete(2)
        # Observation Space
        self.observation_space = spaces.Box(low=0, high=1, shape=(int(self.shape[1]) - 1, ), dtype=np.float32)
        
        self.current_step = 0
        self.max_steps = max_steps
        
    
    # Define Step Function
    def step(self, action):
        done = False
        reward = int(action == self.expected_action)
        self.current_step += 1
        full_row = self.Dataframe.iloc[self.current_step].values
        new_state = full_row[:-1]
        self.expected_action = full_row[-1]
        if self.current_step == self.max_steps:
            done: True
        return new_state, reward, done, {}, {}
    
    
    def reset(self):
        self.Dataframe = self.Dataframe.sample(frac=1).reset_index()
        self.current_step = 0
        full_row = self.Dataframe.iloc[self.current_step].values
        start_state = full_row[:-1]
        self.expected_action = full_row[-1]
        return start_state, {}
    