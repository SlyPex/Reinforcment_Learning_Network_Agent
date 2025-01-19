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
        # Observation Space
        self.observation_space = spaces.Box(low=0, high=1, shape=(41,), dtype=np.float32)
        
    # Define Step Function
    def step(self, action):
        return super().step(action)
    def reset(self, *, seed = None, options = None):
        return super().reset(seed=seed, options=options)
    