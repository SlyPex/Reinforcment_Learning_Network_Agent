import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

# Define NetworkDefence Class
class NetworkDefence(gym.Env):
    def __init__(self, ):
        super(NetworkDefence, self).__init__()
        # Action Space : 0 - Allow | 1 - Deny
        self.action_space = spaces.Discrete(2)
        # TODO: Define the Observation Space 
        
    # Define Step Function
    def step(self, action):
        return super().step(action)
    def reset(self, *, seed = None, options = None):
        return super().reset(seed=seed, options=options)
    