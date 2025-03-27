class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def valid(gap):
            k = m - 1
            prev = position[0]
            for i in range(len(position)):
                if position[i]-prev >= gap:
                    k -= 1
                    prev = position[i]
            return k <= 0


        l = 1
        r = ceil(max(position))        
        ans = -1     
        while l<=r:
            mid = (l+r)//2
            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans