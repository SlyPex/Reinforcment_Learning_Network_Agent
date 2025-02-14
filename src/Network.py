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
        self.observation_space = spaces.Box(low=0, high=1, shape=(int(self.shape[1]) - 1, ), dtype=np.float64)
        self.taken_action = []
        self.current_step = 0
        self.max_steps = max_steps
        
    
    # Define Step Function
    def step(self, action):
        terminated = False
        truncated = False
        reward = int(action == self.expected_action)
        self.current_step += 1
        if self.current_step < len(self.Dataframe):
            full_row = self.Dataframe.iloc[self.current_step].values
            new_state = full_row[:-1].copy()
            self.expected_action = full_row[-1]
        else:
            # If we exceed the dataset, terminate
            new_state = None
            terminated = True
        if self.current_step >= self.max_steps:
            truncated = True
        return new_state, reward, terminated, truncated, {}
    
    # Define Reset Function
    def reset(self, *, seed = None, options = None):
        self.Dataframe = self.Dataframe.sample(frac=1).reset_index(drop=True)
        self.current_step = 0
        full_row = self.Dataframe.iloc[self.current_step].values
        init_state = full_row[:-1].copy()
        self.expected_action = full_row[-1]
        return init_state, {}