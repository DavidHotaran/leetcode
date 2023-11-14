# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # method 1: 2 pointers M = O(1)
        if head == None:
            return False

        p1 = head
        p2 = head.next

        while p2 and p2.next:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False

        # method 2 with set M = O(n)
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
