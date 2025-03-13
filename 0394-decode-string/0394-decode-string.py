class Solution:
    def decode(self,i:int, s: str) -> str:
        decodedStr=""
        mul=0
        while i<len(s):
            ch=s[i]
            if ch.isdigit():
                mul=mul*10+int(ch)
            elif ch=="[":
                innerDecodedStr,i=self.decode(i+1,s)
                decodedStr+=mul*innerDecodedStr
                mul=0
            elif ch=="]":
                return decodedStr,i
            else:
                decodedStr+=ch
            i+=1
        return decodedStr,i

    def decodeString(self, s: str) -> str:
        return self.decode(0,s)[0]
       

