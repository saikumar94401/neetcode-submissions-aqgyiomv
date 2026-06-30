class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def sellStock(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            temp=0
            if buy==-1 :
                temp+=sellStock(i+1,i)
            elif prices[i]>prices[buy]:
                temp+=(prices[i]-prices[buy])+sellStock(i+2,-1)

            memo[(i,buy)]=temp=max(temp,sellStock(i+1,buy))
            return temp




        return sellStock(0,-1)