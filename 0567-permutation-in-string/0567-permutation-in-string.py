class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        hm=dict(Counter(s1))
        window=dict(Counter(s2[:n]))
        l,r=0,n-1
      

        while r<len(s2)-1:
            r+=1
            if hm==window:
                return True
            if s2[r] in window:
                window[s2[r]]+=1
            else:
                window[s2[r]]=1
            del window[s2[l]]
            l+=1
           
            print(window)
        return False




        
        