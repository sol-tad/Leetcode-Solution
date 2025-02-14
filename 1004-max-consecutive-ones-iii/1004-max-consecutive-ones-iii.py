class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        res=0
        zero=0
        for r in range(len(nums)):

            if nums[r]==1:
                res=max(res,r-l+1)
                continue
            elif nums[r]==0:
                zero+=1
                if zero<=k:
                    continue
                else:   
                    res=max(res,r-l)
                    while zero>k:
                        print(l)
                        if nums[l]==0:
                            zero-=1
                        l+=1     
        return res

            
        