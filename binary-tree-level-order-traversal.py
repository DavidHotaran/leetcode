# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []
        queue = [[root]]

        while queue:
            node = queue.pop()
            values = []
            temp = []

            for i in node:
                if i:
                    values.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp:
                queue.append(temp)
            if values:
                ret.append(values)
        return ret
