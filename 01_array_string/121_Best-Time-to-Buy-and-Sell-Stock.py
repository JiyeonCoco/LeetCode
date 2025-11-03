class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = prices[0]

        for p in prices[1:]:

            if p < min_price:
                min_price = p

            else:
                cur_profit = p - min_price

                if cur_profit > max_profit:
                    max_profit = cur_profit

        return max_profit
