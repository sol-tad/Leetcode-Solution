class Solution:
    def checkString(self, s: str) -> bool:
        sl=list(s)
        turn=-1
        if s.count('a')==0 or s.count('b')==0:
            return True
        else:
            for i in range(len(s)):
                if s[i]=='b':
                    turn=i
                    break
            if s[turn:len(s)].count('a')>0:
                return False
        return True


       