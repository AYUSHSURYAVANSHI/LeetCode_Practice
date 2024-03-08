<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        p, q, curr_sum = l1, l2, sum_head
        carry = 0
        while p or q or carry:
            p, p_val = (p.next, p.val) if p else (p, 0)
            q, q_val = (q.next, q.val) if q else (q, 0)
            carry, sum_ = divmod(p_val + q_val + carry, 10)
            curr_sum.next = ListNode(sum_)
            curr_sum = curr_sum.next
=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        p, q, curr_sum = l1, l2, sum_head
        carry = 0
        while p or q or carry:
            p, p_val = (p.next, p.val) if p else (p, 0)
            q, q_val = (q.next, q.val) if q else (q, 0)
            carry, sum_ = divmod(p_val + q_val + carry, 10)
            curr_sum.next = ListNode(sum_)
            curr_sum = curr_sum.next
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return sum_head.next