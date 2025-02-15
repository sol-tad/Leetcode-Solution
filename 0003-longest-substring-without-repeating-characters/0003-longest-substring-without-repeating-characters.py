class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        currcount=0
        hm=defaultdict(int)
        l=0

        for r in range(len(s)):
            currcount+=1
            hm[s[r]]+=1
            while hm[s[r]]>1:
                hm[s[l]]-=1
                if hm[s[l]]==0:
                    del hm[s[l]]
                l+=1
                currcount-=1   
            maxlen=max(maxlen,currcount)
        return maxlen
