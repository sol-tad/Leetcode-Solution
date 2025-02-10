class Solution:
    def frequencySort(self, s: str) -> str:
        hm=dict(Counter(s))
        sortedHm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))   
        res=""
        for k in sortedHm:
            res+=k*sortedHm[k]
        return res

        