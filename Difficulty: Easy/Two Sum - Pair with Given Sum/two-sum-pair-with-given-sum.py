class Solution:
    def twoSum(self, arr: list[int], target: int) -> bool:
        seen = set()
        
        for num in arr:
            complement = target - num
            
            if complement in seen:
                return True
            
            seen.add(num)
            
        return False