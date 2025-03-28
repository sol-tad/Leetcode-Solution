class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm={}
        for n in nums:
            if n in hm:
                hm[n]+=1
            else:
                hm[n]=1
        
        
        shm= {key:val for key,val in sorted(hm.items(),key=lambda item:item[1])}
        res=list(shm.keys())
        print(res)
        return res[-k:]

        