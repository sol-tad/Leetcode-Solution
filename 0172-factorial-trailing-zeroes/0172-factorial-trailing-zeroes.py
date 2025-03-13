class Solution:
    def factorial(self,n):
        if n==0 or n==1:
            return 1 
        return n*self.factorial(n-1)

    def trailingZeroes(self, n: int) -> int:
        ans=self.factorial(n)
        count=0
        while ans%10==0:
            count+=1
            ans//=10

        return count


        