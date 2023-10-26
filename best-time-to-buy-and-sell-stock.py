class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_so_far = float("inf")

        for i in prices:
            # want to find smallest stock
            # and largest stock AFTER
            # keep track of min price so far
            min_so_far = min(min_so_far, i)
            temp = i - min_so_far
            profit = max(profit, temp)
        return profit
