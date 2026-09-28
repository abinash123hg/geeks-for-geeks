import math

class SegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr: list[int], node: int, start: int, end: int):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        self._build(arr, left_node, start, mid)
        self._build(arr, right_node, mid + 1, end)
        self.tree[node] = math.gcd(self.tree[left_node], self.tree[right_node])

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        if start <= idx <= mid:
            self.update(left_node, start, mid, idx, val)
        else:
            self.update(right_node, mid + 1, end, idx, val)
            
        self.tree[node] = math.gcd(self.tree[left_node], self.tree[right_node])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # Range representation completely outside query range
        if r < start or end < l:
            return 0
        # Range representation completely inside query range
        if l <= start and end <= r:
            return self.tree[node]
            
        mid = (start + end) // 2
        left_gcd = self.query(2 * node + 1, start, mid, l, r)
        right_gcd = self.query(2 * node + 2, mid + 1, end, l, r)
        
        return math.gcd(left_gcd, right_gcd)


class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        st = SegmentTree(arr)
        result = []
        
        for q in queries:
            type_q = q[0]
            if type_q == 0:
                l, r = q[1], q[2]
                result.append(st.query(0, 0, n - 1, l, r))
            elif type_q == 1:
                idx, val = q[1], q[2]
                st.update(0, 0, n - 1, idx, val)
                
        return result