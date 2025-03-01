class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1set=set(nums1)
        num2set=set(nums2)
        res=[]
        res.append(list(num1set-num2set))
        res.append(list(num2set-num1set))
        return res