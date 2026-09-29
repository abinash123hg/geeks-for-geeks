class Solution:
    def perfectSum(self, arr, target):
        # dp[j] will store the number of subsets with sum equal to j
        dp = [0] * (target + 1)
        
        # Base case: There is 1 subset with sum 0 (the empty subset)
        dp[0] = 1
        
        for num in arr:
            # Traverse backwards to use values from the previous iteration
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[target]