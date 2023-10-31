# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [[root]]
        ret = []

        while queue:
            node = queue.pop()
            temp = 0
            num = 0
            values = []
            for i in node:
                if i:
                    num += 1
                    temp += i.val
                    values.append(i.left)
                    values.append(i.right)
            if values:
                # print(temp, node)
                avg = temp / num
                queue.append(values)
                ret.append(avg)
        return ret
