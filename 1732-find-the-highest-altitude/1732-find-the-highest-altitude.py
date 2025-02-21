class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1,len(gain)):
            gain[i]+=gain[i-1]
        if max(gain)<0:
            return 0
        else:
            return max(gain)