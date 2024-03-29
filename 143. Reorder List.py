<<<<<<< HEAD

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            # Save next pointers
            tmp1 = first.next
            tmp2 = second.next
            
            # Reorder nodes
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
=======

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            # Save next pointers
            tmp1 = first.next
            tmp2 = second.next
            
            # Reorder nodes
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
            second = tmp2