class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        idx=len(s)-1
        size=0
        slist=list(s)
        if s[-1].isdigit():
            idx=len(s)-2
        
        if len(s)%2==0:
            size=len(s)//2
        else:
            if s[0].isdigit():
                size=len(s)//2
            else:
                size=(len(s)//2)+1
        res=[]
        for i in range(2**size):
            curr=slist.copy()
            k=idx
            while i>0 and k>=0:
                if i&1:
                    curr[k]=curr[k].upper()
                i>>=1
                k-=2
            res.append("".join(curr))
        return res

           
        


