class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close_needed,open_needed=0,0
        for c in s:
            if c=='(':
                close_needed+=1
            else:
                if close_needed>0:
                    close_needed-=1
                else:
                    open_needed+=1
        return (close_needed+open_needed)


        