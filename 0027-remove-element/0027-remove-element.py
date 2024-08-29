class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)-nums.count(val)
        i=len(nums)-1
        while i>=0:
            if nums[i]==val:
                nums.pop(i)
                # i-=1
            i-=1
        return k
        