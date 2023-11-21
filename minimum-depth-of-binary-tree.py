# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        queue = [[root]]

        while queue:
            nodes = queue.pop()
            temp = []
            for node in nodes:
                if not node:
                    continue

                if not node.left and not node.right:
                    return depth

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

                if temp:
                    queue.append(temp)

            depth += 1
        return depth
