# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = []
        ret = float("inf")

        def in_order(root):
            if root:
                in_order(root.left)
                queue.append(root.val)
                in_order(root.right)

        in_order(root)
        for i in range(len(queue) - 1):
            temp = abs(queue[i] - queue[i + 1])
            ret = min(ret, temp)
        return ret
