#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowest_price = prices[0]
        max_profit = 0
        for p in prices:
            lowest_price = min([lowest_price, p])
            max_profit = max([max_profit, p - lowest_price])
        return max_profit
