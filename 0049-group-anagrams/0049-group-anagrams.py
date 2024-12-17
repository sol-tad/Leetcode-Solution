class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            hv=str(sorted(list(s)))
            if hv in hm:
                hm[hv].append(s)
            else:
                hm[hv]=[s]
        return list(hm.values())


    
        
        