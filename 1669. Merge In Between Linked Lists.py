<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        temp1 = list1
        curr = list1
        a -= 1  # Adjust a to match zero-based indexing
        
        # Traverse list1 to find the node at position (a-1)
        while temp1 and a > 0:
            temp1 = temp1.next
            prev = temp1
            a -= 1
        
        temp1 = list1  # Reset temp1 to traverse list1 again
        
        # Traverse list1 to find the node at position (b+1)
        while temp1 and b > 0:
            temp1 = temp1.next
            curr = temp1
            b -= 1
        
        temp2 = list2  # Initialize pointer to traverse list2
        
        # Traverse list2 to find the last node
        while temp2.next:
            temp2 = temp2.next
        
        prev.next = list2  # Connect the node before position 'a' to the head of list2
        temp2.next = curr.next  # Connect the last node of list2 to the node after position 'b'
        
=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        temp1 = list1
        curr = list1
        a -= 1  # Adjust a to match zero-based indexing
        
        # Traverse list1 to find the node at position (a-1)
        while temp1 and a > 0:
            temp1 = temp1.next
            prev = temp1
            a -= 1
        
        temp1 = list1  # Reset temp1 to traverse list1 again
        
        # Traverse list1 to find the node at position (b+1)
        while temp1 and b > 0:
            temp1 = temp1.next
            curr = temp1
            b -= 1
        
        temp2 = list2  # Initialize pointer to traverse list2
        
        # Traverse list2 to find the last node
        while temp2.next:
            temp2 = temp2.next
        
        prev.next = list2  # Connect the node before position 'a' to the head of list2
        temp2.next = curr.next  # Connect the last node of list2 to the node after position 'b'
        
>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
        return list1  # Return the head of list1