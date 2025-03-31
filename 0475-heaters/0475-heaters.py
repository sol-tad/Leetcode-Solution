class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res=float('-inf')
        for house in houses:
            i=bisect_left(heaters,house)
            if i==0:
                res=max(res,abs(house-heaters[i]))
            elif i>=len(heaters):
                res=max(res,abs(house-heaters[i-1]))
            else:
                currmin=min(abs(house-heaters[i-1]),abs(house-heaters[i]))
                res=max(res,currmin)
        return res

