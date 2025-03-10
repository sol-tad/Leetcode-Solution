def powOfFour(num,n)->bool:
    
    if num==1:
        return True
    elif num<1:
        return False
    return powOfFour(num/4,n)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ans=powOfFour(n,n)
        return ans