class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        
        for i in range(1, len(prices)):
            temp_cash = cash
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, temp_cash - prices[i])
            
        return cash