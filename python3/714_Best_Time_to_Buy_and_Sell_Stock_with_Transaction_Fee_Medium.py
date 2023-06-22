# 714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        has_stock = -prices[0] - fee
        no_stock = 0

        for i in range(1, len(prices)):
            temp_has_stock = max(no_stock - prices[i] - fee, has_stock)
            temp_no_stock = max(no_stock, has_stock + prices[i])
            has_stock = temp_has_stock
            no_stock = temp_no_stock

        return max(has_stock, no_stock)
