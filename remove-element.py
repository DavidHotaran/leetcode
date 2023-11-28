class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        for i in range(len(nums)):
            """
            when we encounter a value that != val, swap. if we encounter val,
            continue. k will stay at that spot until we find a number that != val, then we swap
            and increment k again,.
            """
            if nums[i] != val:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k += 1
        return k
