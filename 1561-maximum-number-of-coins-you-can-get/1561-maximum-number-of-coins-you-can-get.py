class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count=0
        alice=len(piles)-1
        me=alice-1
        bob=0
        piles.sort()
        while bob<me:
            count+=piles[me]
            bob+=1
            me-=2
        return count

        
        