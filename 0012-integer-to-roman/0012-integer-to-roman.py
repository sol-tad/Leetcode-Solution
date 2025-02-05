class Solution:
    def intToRoman(self, num: int) -> str:
        hm = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        mul=len(str(num))-1
        roman=""
        while num>0:
            currdigit=num//(10**mul)
            if currdigit!=4 and currdigit!=9 and currdigit<5:
                roman+=hm[10**mul]*currdigit
            elif currdigit!=4 and currdigit!=9 and currdigit>=5:
                roman+=hm[5*(10**mul)]+hm[10**mul]*(currdigit-5)
            elif currdigit==4:
                roman+=hm[10**mul]+hm[5*(10**mul)]
            elif currdigit==9:
                roman+=hm[10**mul]+hm[10**(mul+1)]
            num=num%(10**mul)
            mul-=1
        return roman


