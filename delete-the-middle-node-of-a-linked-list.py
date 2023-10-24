# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head.next

        p1, p2 = head, head
        temp = p1

        while p2 and p2.next:
            temp = p1
            p1 = p1.next
            p2 = p2.next.next
        temp.next = p1.next
        return head
