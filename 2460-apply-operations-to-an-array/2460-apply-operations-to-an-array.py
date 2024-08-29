class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        j=i+1
        while j<len(nums) and i<j:
            if nums[i]==nums[j] and nums[i]!=0:
                nums[i]*=2
                nums[j]=0
                a.append(nums[i])
            elif nums[i]!=0:
                 a.append(nums[i])
            elif j==len(nums)-1 and nums[j]!=0 and nums[j]!=nums[j-1]:
                 a.append(nums[j])
            j+=1
            i+=1

        if len(nums)<=2:
            nums[0],nums[1]=nums[1],nums[0]
            return nums
        for i in range(len(nums)-len(a)):
            a.append(0)
        return a


      