class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hm={}
        res=[]
        for i in range(len(cpdomains)):
            index = cpdomains[i].find(" ")
            num=int(cpdomains[i][:index])
            domain=cpdomains[i][index+1:].split(".")
            currdomain=domain[-1]
            if currdomain in hm:
                    hm[currdomain]+=num
            else:
                     hm[currdomain]=num
           
            for j in range(len(domain)-2,-1,-1):
                currdomain=domain[j]+"."+currdomain
                if currdomain in hm:
                    hm[currdomain]+=num
                else:
                     hm[currdomain]=num        
                
        for key in hm:
            res.append(str(hm[key])+" "+key)
        return res

            