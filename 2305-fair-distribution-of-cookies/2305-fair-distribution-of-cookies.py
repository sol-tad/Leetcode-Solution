class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res=float("inf")
        def bk(i,childs):
            nonlocal res
            # print(childs)
            if i==len(cookies):
                res=min(res,max(childs))
                return
            
            for ch in range(k):
                childs[ch]+=cookies[i]
                if res>childs[ch]:
                    bk(i+1,childs)
                childs[ch]-=cookies[i]
        bk(0,[0]*k)
        return res