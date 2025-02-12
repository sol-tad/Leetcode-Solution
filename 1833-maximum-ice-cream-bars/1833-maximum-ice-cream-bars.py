class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        costs.sort()
        if costs[0]>coins:
            return 0
        else:
            costsum=0
            for c in costs:
                costsum+=c
                if costsum<=coins:
                    count+=1
        return count
