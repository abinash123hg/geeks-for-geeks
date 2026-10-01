''' Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.next = None
        self.data = val
'''

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        # Step 1: Detect cycle using slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        # If no loop exists
        if slow != fast:
            return
            
        # Step 2: Find the starting node of the loop
        # Case A: Loop starts at the head node
        if slow == head:
            while fast.next != head:
                fast = fast.next
            fast.next = None
            return
            
        # Case B: Loop starts somewhere inside the list
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
            
        # Step 3: Break the loop
        fast.next = None