class Solution:
    def minInsertions(self, s: str) -> int:
        missing = 0
        open = 0

        i = 0
        while i <= len(s) - 1:
            if s[i] == '(':
                open += 1
            else:
                j = i
                while j + 1 < len(s) and s[j + 1] == ')':
                    j += 1
                total = j - i + 1
                fullClosed = total // 2
                halfClosed = total % 2

                for _ in range(fullClosed):
                    if open:
                        open -= 1
                    else:
                        missing += 1
                
                if halfClosed:
                    if open:
                        missing += 1
                        open -= 1
                    else:
                        missing += 2
                i = j
            i += 1
        
        return missing + open * 2
