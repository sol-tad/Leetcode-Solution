class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for r in range(len(accounts)):
            currsum=0
            for w in range(len(accounts[r])):
                currsum+=accounts[r][w]
            maxwealth=max(maxwealth,currsum)
        return maxwealth
