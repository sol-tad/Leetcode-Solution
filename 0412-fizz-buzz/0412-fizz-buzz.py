class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        i=0
        while i<n:
            if (i+1)%3==0 and (i+1)%5==0:
                ans.append("FizzBuzz")
            elif (i+1)%3==0:
                ans.append("Fizz")
            elif (i+1)%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i+1))
            i+=1
        return ans