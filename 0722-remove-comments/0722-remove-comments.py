class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        inBlockComment = False
        result = []
        newLine = []
    
        for line in source:
            i = 0
            if not inBlockComment:
                newLine = [] 

            while i < len(line):
                if not inBlockComment:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        inBlockComment = True
                        i += 1  
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break  
                    else:
                        newLine.append(line[i])
                else:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        inBlockComment = False
                        i += 1 
                i += 1

            if newLine and not inBlockComment:
                result.append("".join(newLine))

        return result