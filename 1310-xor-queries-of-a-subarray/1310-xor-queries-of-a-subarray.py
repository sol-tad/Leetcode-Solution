class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(1,len(arr)):
            arr[i]^= arr[i-1]
        for a,b in queries:
            if a==0:
                ans.append(arr[b])
            else:
                ans.append(arr[a-1]^arr[b])
        return ans    