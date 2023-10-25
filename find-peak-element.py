class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 1, len(nums) - 2

        while l <= r:
            mid = (l + r) // 2
            left = nums[mid - 1]
            right = nums[mid + 1]
            # print(left, right, mid)

            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] > left:
                l = mid + 1
            else:
                r = mid - 1
