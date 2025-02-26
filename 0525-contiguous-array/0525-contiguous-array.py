class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zerocount=0
        onecount=0
        hm=defaultdict(int)#stores onecount - zerocount with curr  index 
        maxlen=0
        for i in range(len(nums)):
            if nums[i]==1:
                onecount+=1
            else:
                zerocount+=1
            
            if (onecount-zerocount) not in hm:
                hm[onecount-zerocount]=i


            if onecount==zerocount:
                 maxlen=max(maxlen,onecount+zerocount)
            elif (onecount-zerocount) in hm:
                maxlen=max(maxlen,i-hm[onecount-zerocount])

 
        return maxlen
            