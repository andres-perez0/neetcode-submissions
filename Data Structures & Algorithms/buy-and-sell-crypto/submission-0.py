class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0

        n = len(prices) - 1
        low = prices[0]

        for i in range(n):                

            curr_profit = 0

            if low < prices[i + 1]:
                curr_profit = prices[i+1] - low

                if curr_profit > profit:
                    profit = curr_profit
            else: 
                low = prices[i + 1]

        return profit

        