class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        rangePsum=[0]*(len(s)+1)
        res=""
        for i,e,f in shifts:
            if f==0:
                rangePsum[i]-=1
                rangePsum[e+1]+=1
            else:
                rangePsum[i]+=1
                rangePsum[e+1]-=1
        
        for i in range(1,len(rangePsum)):
            rangePsum[i]+=rangePsum[i-1]
        print(rangePsum)

        for i in range(len(s)): 
            res+=chr(((ord(s[i])-ord('a')+rangePsum[i]) % 26)+ord('a'))

        return res




        