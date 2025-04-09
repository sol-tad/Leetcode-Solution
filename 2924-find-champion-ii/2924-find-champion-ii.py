class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # indegree=set()
        # outdegree=set()
        # for a,b in edges:
        #     if a not in indegree:
        #         outdegree.add(a)
        #     elif a in indegree and  a in outdegree:
        #         outdegree.remove(a)
        #     indegree.add(b)
        # # print( outdegree)
        # # print( indegree)
        # res=-1
        # if n==1:
        #     return 0
        # if len(outdegree)==1:
        #     for i in outdegree:
        #         res=i
        # return res
        graph=defaultdict(list)
        indegree=[0]*n
        print(graph)
        for a,b in edges:
            graph[a].append(b)
        def dfs(node):
            for adj in graph[node]:
                if indegree[adj]==0:
                    indegree[adj]=1
                    dfs(adj)
        print(indegree)
        count=0
        res=-1
        for i in range(n):
            if not indegree[i]:
                dfs(i)
        for team in range(n):
            if indegree[team] ==0:
                count+=1
                res=team
            if count>=2:
                return -1
        return res
            


# class Solution:
#     def findChampion(self, n: int, edges: List[List[int]]) -> int:
#         adj = defaultdict(list)

#         for u ,v in edges:
#             adj[u].append(v)

#         seen = [0] * n

#         def dfs(node):

#             for ch in adj[node]:
#                 if not seen[ch]:
#                     seen[ch] = 1
#                     dfs(ch)


#         cnt = 0
#         for i in range(n):
#             if not seen[i]:
#                 dfs(i)

#         ans = -1
#         for i , n in enumerate(seen):
#             if not n and ans != -1:
#                 return -1
#             if not n:
#                 ans = i
        
#         return ans


            
            
