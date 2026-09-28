class Solution:
    def isBST(self, root: 'Node') -> bool:
        prev = float('-inf')
        
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Current value must be strictly greater than previous value
            if node.data <= prev:
                return False
            prev = node.data
            
            # Check right subtree
            return inorder(node.right)
            
        return inorder(root)