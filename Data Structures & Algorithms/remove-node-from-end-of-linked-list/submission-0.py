# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        l1 = reverse(head)
        dummy = ListNode(-1, l1)
        curr = dummy
        for _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next
        l2 = reverse(dummy.next)
        return l2