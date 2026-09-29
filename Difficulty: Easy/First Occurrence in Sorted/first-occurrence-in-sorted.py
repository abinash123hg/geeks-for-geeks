class Solution:
    def firstSearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                ans = mid
                high = mid - 1  # Continue searching in the left half for the first occurrence
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return ans