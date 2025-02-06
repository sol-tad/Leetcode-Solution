class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hm=dict(Counter(nums))
        rem=0
        pair=0
        if len(nums)==1:
            return [0,1]
        for k in hm:
            if hm[k]==2:
                pair+=1
            elif hm[k]%2==0:
                pair+=hm[k]//2
            else:
                if hm[k]>2 and  hm[k]%2!=0:
                    pair+= hm[k]//2
                    rem+= hm[k]%2
        return [pair,rem]
        