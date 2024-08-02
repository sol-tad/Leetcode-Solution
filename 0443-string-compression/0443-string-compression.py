class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        s = []
        length = 0
        curr = chars[0]
        if len(chars)==1:
            return 1
        while i < len(chars):
            if chars[i] == curr:
                length += 1
                i += 1
            else:
                s.append(curr)
                
                lenStr = str(length)
                if len(lenStr) < 2:
                    if length>1:
                     s.append(lenStr)
                else:
                    for j in range(len(lenStr)):
                        s.append(lenStr[j])
                if i < len(chars):  
                    curr = chars[i]
                length = 0
        s.append(curr)
        lenStr = str(length)
        if len(lenStr) < 2:
            if length>1:
             s.append(lenStr)
        else:
            for j in range(len(lenStr)):
                s.append(lenStr[j])

        chars.clear()
        chars.extend(s)
        print(s)
        return len(chars)