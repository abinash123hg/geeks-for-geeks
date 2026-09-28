class Solution:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        visited = [False] * V
        rec_stack = [False] * V
        
        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            
            for neighbor in adj[u]:
                # If neighbor is not visited, recursively visit it
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                # If neighbor is already in the current recursion stack, cycle found
                elif rec_stack[neighbor]:
                    return True
            
            # Remove vertex from recursion stack before returning
            rec_stack[u] = False
            return False
            
        # Step 2: Check for cycles in all connected components
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
                    
        return False