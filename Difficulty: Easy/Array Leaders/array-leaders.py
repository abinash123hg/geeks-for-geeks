class Solution:
    def leaders(self, arr):
        res = []
        max_from_right = float('-inf')
        
        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_from_right:
                res.append(arr[i])
                max_from_right = arr[i]
                
        # Reverse the result array to restore original left-to-right order
        return res[::-1]