# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        prev = None
        curr = mid
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        l1 = head
        l2 = prev

        while l2:
            nextl1 = l1.next
            nextl2 = l2.next

            l1.next = l2
            l2.next = nextl1

            l1=nextl1
            l2=nextl2