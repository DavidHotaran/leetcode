class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = total = sum(nums[:k])

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            total = max(total, curr)
        return total / k
