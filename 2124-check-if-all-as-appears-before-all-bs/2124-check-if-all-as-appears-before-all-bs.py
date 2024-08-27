class Solution:
    def checkString(self, s: str) -> bool:
        flag = True
        turn = 0
        i = 0
        
        if s.count('a') == len(s):
            return True
        else:
            while i < len(s) - 1 and s[i] == 'a':
                turn = i
                i += 1

            i = turn + 1
            while i < len(s):
                if s[i] == 'a':
                    flag = False
                    break
                i += 1
        
        return flag
