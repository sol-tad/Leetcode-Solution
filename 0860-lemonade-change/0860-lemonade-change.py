class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hm={5:0,10:0}
        for b in bills:
            if b==5:
                hm[5]+=1
            elif b==10:
                if hm[5]>=1:
                    hm[5]-=1
                    hm[10]+=1
                else:
                    return False
            elif b==20:
                if hm[5]>=1 and hm[10]>=1:
                    hm[5]-=1
                    hm[10]-=1
                elif hm[5]>=3:
                    hm[5]-=3
                else:
                    return False
        return True
        