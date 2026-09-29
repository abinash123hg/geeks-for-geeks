class Solution:
    def setBit(self, n):
        # Bitwise OR with (n + 1) sets the rightmost unset bit
        return n | (n + 1)