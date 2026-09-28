from collections import Counter

class Solution:
    def isSubset(self, a: list[int], b: list[int]) -> bool:
        # Count frequency of each element in array 'a'
        freq_a = Counter(a)
        # Count frequency of each element in array 'b'
        freq_b = Counter(b)
        
        # Check if array 'a' has at least as many instances of each element in 'b'
        for num, count in freq_b.items():
            if freq_a[num] < count:
                return False
                
        return True