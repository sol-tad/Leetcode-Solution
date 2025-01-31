class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num=[]
        for n in nums:
            num.append(int(n))
        num.sort()
        return str(num[-k])
        
