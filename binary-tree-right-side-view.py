# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = [root.val]
        queue = [[root]]

        while queue:
            temp = []
            nodes = queue.pop()
            for node in nodes:
                if node and node.left:
                    temp.append(node.left)
                if node and node.right:
                    temp.append(node.right)
            if temp:
                ret.append(temp[-1].val)
                queue.append(temp)
        return ret
