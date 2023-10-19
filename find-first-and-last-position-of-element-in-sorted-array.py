class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ret = [-1, -1]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
               ret[0] = mid
               right = mid -1
            elif nums[mid] < target:
                left = mid + 1 
            elif nums[mid] > target:
                right = mid -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
               ret[1] = mid
               left = mid + 1
            elif nums[mid] < target:
                left = mid + 1 
            elif nums[mid] > target:
                right = mid -1
        
        return ret