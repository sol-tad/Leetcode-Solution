# import sys
# sys.setrecursionlimit(3000)

class Solution:
    def kth(self,n,k):
        if n==1:
            return '0'

        ans=self.kth(n-1,(k+1)//2)
        
        if ans=='0':
            if k%2==0:
                return '1'
            else:
                return "0"
        else:
            if k%2==0:
                return '0'
            else:
                return "1"

    def kthGrammar(self, n: int, k: int) -> int:
        
        return int(self.kth(n,k))
        