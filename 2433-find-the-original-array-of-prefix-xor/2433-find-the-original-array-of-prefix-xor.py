class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[0]*len(pref)
        for i in range(len(pref)):
            if i==0:
                ans[0]=pref[0]
            else:
                ans[i]=pref[i]^pref[i-1]
        return ans