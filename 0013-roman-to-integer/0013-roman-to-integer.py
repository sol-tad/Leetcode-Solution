class Solution:
    def romanToInt(self, s: str) -> int:
        roman=s.upper()
        converted_roman=[]
        for i in range(len(roman)):
            if roman[i]=="I":converted_roman.append(1)
            if roman[i]=="V":converted_roman.append(5)
            if roman[i]=="X":converted_roman.append(10)
            if roman[i]=="L":converted_roman.append(50)
            if roman[i]=="C":converted_roman.append(100)
            if roman[i]=="D":converted_roman.append(500)
            if roman[i]=="M":converted_roman.append(1000)
        numeric_value=0
        print(converted_roman)
        i=0
        while i<len(converted_roman)-1:
            if converted_roman[i]<converted_roman[i+1]:
                numeric_value+=converted_roman[i+1]-converted_roman[i]
                i=i+1
            else:numeric_value+=converted_roman[i]
            i=i+1
        if len(converted_roman)>1 and converted_roman[-1]>converted_roman[-2]:
            return numeric_value 
        else :return numeric_value +converted_roman[-1]