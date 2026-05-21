class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            min_pt=prices[i]
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    max_pt=prices[j]
                    profit=max(profit,max_pt-min_pt)
                
        return profit
        