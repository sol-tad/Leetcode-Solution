class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minPrefixSum=float('inf')
        maxPrefixSum=float('-inf')
        psum=maxsum=0

        for num in nums:
            psum+=num

            minPrefixSum=min(minPrefixSum,psum)
            maxPrefixSum=max(maxPrefixSum,psum)

            if psum>=0:
                maxsum=max(maxsum,psum,psum-minPrefixSum)
            elif psum<0:
                maxsum=max(maxsum,abs(psum),abs(psum-maxPrefixSum))
        return maxsum