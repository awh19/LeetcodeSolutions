class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay = 0
        sellDay = 1
        
        if len(prices) == 1:
            return 0
        
        while buyDay < len(prices) and sellDay < len(prices):
            if prices[buyDay] > prices[sellDay]:
                buyDay += 1
                sellDay = buyDay + 1
            else:
                profit = prices[sellDay] - prices[buyDay]
                maxProfit = max(profit,maxProfit)
                sellDay += 1
        
        return maxProfit
            
# Could also do dynamic programming seen below:
    
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minProfit = prices[0]
        
        for i in range(1,len(prices)):
            minProfit = min(minProfit,prices[i])
            maxProfit = max(maxProfit,prices[i]-minProfit)
        
        return maxProfit