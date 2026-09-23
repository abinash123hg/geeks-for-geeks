class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        
        # Step 1: Boyer-Moore Voting Algorithm to find potential majority candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                
        # Step 2: Verify if the candidate actually appears > len(arr) // 2 times
        actual_count = arr.count(candidate)
        if actual_count > len(arr) // 2:
            return candidate
            
        return -1