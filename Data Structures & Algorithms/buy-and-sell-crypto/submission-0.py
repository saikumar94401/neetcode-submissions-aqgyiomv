class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        max_profit=0
        n=len(prices)
        right_max=prices[n-1]
        for i in range(n-2,-1,-1):
            profit = right_max-prices[i]
            if profit>max_profit:
                max_profit=profit
            if prices[i]>right_max: 
                right_max=prices[i]
        return max_profit