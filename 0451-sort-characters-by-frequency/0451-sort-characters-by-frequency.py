class Solution:
    def frequencySort(self, s: str) -> str:
        hm=dict(Counter(s))
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))   
        res=""
        for k in hm:
            res+=k*hm[k]
        return res

        