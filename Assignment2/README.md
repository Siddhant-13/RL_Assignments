# Multi-Armed Bandit Algorithms

### Results Visualization

![Bandit Algorithm Performance](.Assignment2\Assignement\mab_comparison.png)

### Result Description

- The **Exploration Only** strategy, which selects arms randomly, incurs the highest cumulative regret and achieves the lowest average reward because it does not leverage accumulated knowledge.
- The **Exploitation Only** strategy quickly favors the best-known arm but often gets stuck in suboptimal choices, leading to moderate regret and reward.
- The **UCB (Upper Confidence Bound)** algorithm effectively balances exploration and exploitation, resulting in significantly lower regret and higher average reward over time, showcasing superior learning and decision-making ability.
