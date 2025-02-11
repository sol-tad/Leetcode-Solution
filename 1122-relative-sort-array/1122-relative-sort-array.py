class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm=dict(Counter(arr1))
        res=[]
        for n in arr2:
            res.extend([n]*hm[n])
            del hm[n]
        hm = dict(sorted(hm.items()))
        print(hm)
        for k in hm:
            res.extend([k]*hm[k])
        return res

        