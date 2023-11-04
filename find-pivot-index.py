class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for index, num in enumerate(nums):
            r -= num
            if l == r:
                return index
            l += num

        return -1
