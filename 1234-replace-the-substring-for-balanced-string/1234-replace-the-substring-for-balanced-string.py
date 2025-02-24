class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        target=n//4
        hm=Counter(s)

        if max(hm.values())==target:
            return 0

        l=0
        minlen=n

        for r in range(n):
            hm[s[r]]-=1

            while max(hm.values())<=target:
                minlen=min(minlen,r-l+1)
                hm[s[l]]+=1
                l+=1
        return minlen

