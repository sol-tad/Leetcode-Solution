class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=set()
        losser=set()
        losserdic=dict() 
        for i in range(len(matches)):
            winner.add(matches[i][0])
            losser.add(matches[i][1])
            losserdic[matches[i][1]] = losserdic.get(matches[i][1], 0) + 1

        winner=winner-losser
        losserlist=[]
        for key, value in losserdic.items():
            if losserdic[key]==1:
                losserlist.append(key)
        return [sorted(list(winner)),sorted(losserlist)]
