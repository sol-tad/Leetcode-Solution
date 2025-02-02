class Solution:
    def maskPII(self, s: str) -> str:
        if any(char.isdigit() for char in s):
            cleanNum=""
            for snum in s:
                if snum.isdigit():
                    cleanNum+=snum
            encNum="***-***-"+cleanNum[-4:]
            if len(cleanNum)>10:
                encNum="+"+("*"*(len(cleanNum)-10))+"-"+encNum
            return encNum

        else:
            s=s.lower()
            encEmail=s[0]+"*****"+s[(s.find("@"))-1]+s[s.find("@"):]
            return encEmail


        