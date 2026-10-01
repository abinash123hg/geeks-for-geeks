class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # dp[w] stores the maximum value achievable with capacity w
        dp = [0] * (W + 1)
        
        # Iterate over all items
        for i in range(len(val)):
            # Iterate backwards through capacities to avoid using the same item multiple times
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
                
        return dp[W]