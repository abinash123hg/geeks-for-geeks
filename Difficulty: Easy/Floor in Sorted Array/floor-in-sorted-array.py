class Solution:
    def findFloor(self, arr: list[int], x: int) -> int:
        low = 0
        high = len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                ans = mid        # Store mid as a valid floor candidate
                low = mid + 1    # Search right for a larger value or last occurrence
            else:
                high = mid - 1   # Search left
                
        return ans