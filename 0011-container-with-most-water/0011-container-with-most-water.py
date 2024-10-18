class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxArea=0
        while l<r:
            curr=(r-l)*min(height[r],height[l])
            maxArea=max(maxArea,curr)
            if height[r]>height[l]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                r-=1
                l+=1
        return maxArea

      