class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0 for _ in nums]
        prefix = [0 for _ in nums]
        postfix = [0 for _ in nums]
        
        temp = 1
        for i in range(len(nums)):
            prefix[i] = nums[i] * temp
            temp = nums[i] * temp

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = nums[i] * temp
            temp = nums[i] * temp
        
        for i in range(len(nums)):
            if i == 0:
                ret[i] = 1 * postfix[i+1]
            elif i == len(nums) -1:
                ret[i] = 1 * prefix[i-1]
            else:
                ret[i] = prefix[i-1] * postfix[i+1]


        return ret