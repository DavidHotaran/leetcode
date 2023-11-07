class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for pos, num in enumerate(nums):
            i = target - num
            if i in d:
                return [d[i], pos]
            d[num] = pos
        return []
