# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if n == 1 and not head.next:
            return None

        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = head
        step = 0

        while step < n:
            fast = fast.next
            step += 1

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
