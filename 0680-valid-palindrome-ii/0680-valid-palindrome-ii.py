class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        flag=0
        while l<=r:
            if s[l]!=s[r]:
                if len(s)==3:
                    flag+=1
                flag+=1
            r-=1
            l+=1
        return True if flag<=1 else False

        