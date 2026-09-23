class Solution:
    def findDuplicates(self, arr):
        res = []
        
        for num in arr:
            index = abs(num) - 1
            if arr[index] < 0:
                res.append(abs(num))
            else:
                arr[index] = -arr[index]
                
        return res