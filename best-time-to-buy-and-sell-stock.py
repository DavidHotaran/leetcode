class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < temp:
                temp = prices[i]
            elif prices[i] - temp > profit:
                profit = prices[i] - temp
        return profit

'''
Based on the fact that we have to sell after we buy and we are trying to maximize profit, we can iterate through the prices and only need to consider two things:
1.) Is this price cheaper than any other price I've seen before?
2.) If I subtract current price by the cheapest price I've found, does this yield a greater profit than what I've seen so far?

A fun thing to note is if #1 is true, then #2 cannot be true as well so there isn't a need to check

'''