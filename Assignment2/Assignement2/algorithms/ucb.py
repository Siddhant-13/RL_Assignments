import numpy as np
from algorithms.base_algorithm import BaseMABAlgorithm

class UCB(BaseMABAlgorithm):
    """
    Upper Confidence Bound (UCB) algorithm
    Balances exploration and exploitation using confidence bounds
    """
    def __init__(self, n_arms: int, c: float = 2.0, **kwargs):
        super().__init__(n_arms, **kwargs)
        self.c = c  # Exploration parameter
        
    def select_arm(self) -> int:
        # 1. Check for unpulled arms
        unpulled_arms = np.where(self.pulls == 0)[0]
        if len(unpulled_arms) > 0:
            return int(unpulled_arms[0])
        # 2. Calculate total pulls
        total_pulls = np.sum(self.pulls)
        # 3. Calculate UCB values
        ucb_values = self.estimates + self.c * np.sqrt(np.log(total_pulls) / self.pulls)
        # 4. Return arm with highest UCB value
        return int(np.argmax(ucb_values))
        # 5. Return arm with highest UCB value
        
        # YOUR CODE HERE
        pass
