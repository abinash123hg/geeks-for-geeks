class Solution:
    def missingNum(self, arr):
        # Size of the array is n - 1, so total numbers n is len(arr) + 1
        n = len(arr) + 1
        
        # Expected sum of first n natural numbers
        expected_sum = n * (n + 1) // 2
        
        # Actual sum of given elements
        actual_sum = sum(arr)
        
        # The difference is the missing number
        return expected_sum - actual_sum