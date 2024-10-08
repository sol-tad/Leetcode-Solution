class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        imbalance = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else: 
                balance -= 1
                
            if balance < 0:
                imbalance = max(imbalance, -balance)
        
        return (imbalance + 1) // 2