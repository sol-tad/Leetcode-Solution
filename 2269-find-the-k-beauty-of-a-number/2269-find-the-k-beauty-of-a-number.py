class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        k_beauty=start=0
        end=k-1
        while start<=len(s)-k:
            divisor=int(s[start:end+1])
            if divisor==0:
                start+=1
            elif num%divisor==0:
                k_beauty+=1
                start+=1
            else:
                start+=1
            end+=1
        return k_beauty