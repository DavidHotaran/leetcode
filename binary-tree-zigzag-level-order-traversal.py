# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[root]]
        ret = [[root.val]]
        level = 0

        while queue:
            nodes = queue.pop()
            values = []
            temp = []

            for node in nodes:
                if node.right:
                    values.append(node.right)
                    temp.append(node.right.val)
                if node.left:
                    values.append(node.left)
                    temp.append(node.left.val)
            if values:
                queue.append(values)
                if level % 2 == 0:  # even = L -> R
                    ret.append(temp)
                else:  # odd = R -> L
                    ret.append(temp[::-1])
            level += 1
        return ret
