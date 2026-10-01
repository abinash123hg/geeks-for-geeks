class Solution:
    def peakElement(self, arr):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check if mid is a peak element
            is_left_smaller = (mid == 0 or arr[mid] > arr[mid - 1])
            is_right_smaller = (mid == len(arr) - 1 or arr[mid] > arr[mid + 1])
            
            if is_left_smaller and is_right_smaller:
                return mid
            
            # If the right neighbor is greater, a peak must exist in the right half
            if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            # Otherwise, a peak must exist in the left half
            else:
                high = mid - 1
                
        return 0