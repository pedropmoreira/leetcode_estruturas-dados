# some time the two pointers will be the same if have a cycle : 
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
            if head == ahead:
                return True
        return False