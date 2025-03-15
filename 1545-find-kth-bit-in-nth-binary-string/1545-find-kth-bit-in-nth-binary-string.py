class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def kthbit(n):
            if n == 1:
                return "0"
            prev=kthbit(n-1)
            inverted=''.join('1' if c=='0' else '0' for c in prev)[::-1] 
            return prev+"1"+inverted  
        return kthbit(n)[k-1]  
