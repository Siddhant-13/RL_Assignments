import numpy as np
from algorithms.base_algorithm import BaseMABAlgorithm

class ExplorationOnly(BaseMABAlgorithm):
    """
    Pure exploration algorithm - randomly selects arms
    """
    def __init__(self, n_arms: int, **kwargs):
        super().__init__(n_arms, **kwargs)
        
    def select_arm(self) -> int:
        """
        ## IMPLEMENT EXPLORATION ONLY ALGORITHM HERE ##
        
        Input: None (uses self.n_arms)
        Output: int - randomly selected arm index (0 to n_arms-1)
        
        Strategy: Pure exploration - randomly select any arm with equal probability
        """
        # Select a random arm
        return np.random.randint(self.n_arms)
        
        # SOLUTION (commented out for students):
        # return np.random.randint(0, self.n_arms) 