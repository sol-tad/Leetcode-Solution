class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=set()
        outdegree=set()
        for a,b in edges:
            if a not in indegree:
                outdegree.add(a)
            elif a in indegree and  a in outdegree:
                outdegree.remove(a)
            indegree.add(b)
        # print( outdegree)
        # print( indegree)
        res=-1

        if len(outdegree)==1:
            for i in outdegree:
                res=i
        return res
           