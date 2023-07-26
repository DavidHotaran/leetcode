class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        curr_sum = 0

        for i in range(0, len(nums)):
            curr_sum = curr_sum + nums[i]
            total = max(curr_sum, total)

            if curr_sum < 0:
                curr_sum = 0

        return total

'''
The idea of Kadane's algorithm is to maintain a variable max_ending_here that stores the maximum 
sum contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of 
contiguous subarray found so far, Everytime there is a positive-sum value in max_ending_here compare 
it with max_so_far and update max_so_far if it is greater than max_so_far.

MAIN IDEA:
- the subarray with negative sum is discarded (by assigning max_ending_here = 0 in code).
- we carry subarray till it gives positive sum.
'''