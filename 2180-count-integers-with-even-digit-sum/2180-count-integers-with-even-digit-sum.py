class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            if i>0 and i<10 and i%2==0:
                count+=1
            else:
                s=list(str(i))
                sums=0
                for n in s:
                    sums+=int(n)
                if sums%2==0:
                    count+=1
        return count



            



        