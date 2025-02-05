class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffcount=0
        index1,index2=-1,-1
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            else:
                diffcount+=1
                if index1==-1:
                    index1=i
                elif index2==-1:
                    index2=i
        if diffcount>2:
            return False
        else:
            s2list=list(s2)
            s2list[index1],s2list[index2]=s2list[index2],s2list[index1]
            return s1=="".join(s2list)
            
