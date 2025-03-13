class Solution:
    def power(self,x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            res=self.power(x,n//2)
            res=res*res
            if n%2==0:
                return res
            else:
                return x*res

    def myPow(self, x: float, n: int) -> float:
           
        ans=self.power(x,abs(n))
        if n<0:
            return 1/ans
        else:
            return ans

        