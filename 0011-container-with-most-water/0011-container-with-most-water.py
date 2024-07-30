class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            w=r-l
            maxArea=max(maxArea,w*min(height[l],height[r]))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxArea