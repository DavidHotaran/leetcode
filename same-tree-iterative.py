# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = [p]
        q_queue = [q]

        while p_queue and q_queue:
            (
                v1,
                v2,
            ) = (
                p_queue.pop(),
                q_queue.pop(),
            )
            if not v1 and not v2:
                continue
            elif not v1 or not v2 or v1.val != v2.val:
                return False
            p_queue.append(v1.left)
            p_queue.append(v1.right)

            q_queue.append(v2.left)
            q_queue.append(v2.right)

        return True
