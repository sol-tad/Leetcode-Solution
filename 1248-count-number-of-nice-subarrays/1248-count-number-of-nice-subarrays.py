class Solution:
   def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    subArray=0
    for left in range(len(nums)-k+1):
        right=left+k-1
        while right<len(nums):
            oddCount=sum(1 for x in nums[left:right+1] if x%2!=0)
            if oddCount==k:
                subArray+=1
            right+=1
    return subArray
