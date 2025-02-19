class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        currsum=0
        hm=defaultdict(int)

        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum==goal:
                count+=1
            if currsum-goal in hm:
                count+=hm[currsum-goal]
            hm[currsum]+=1
        return count
