# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = [[root]]

        while queue:
            nodes = queue.pop()
            temp = []
            for node in nodes:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
            if temp:
                depth += 1
                queue.append(temp)
        return depth


# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
