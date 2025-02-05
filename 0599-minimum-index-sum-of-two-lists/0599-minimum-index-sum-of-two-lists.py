class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm=defaultdict(int)
        res=[]

        for i in range(len(list1)):
            if list1[i] in list2:
                hm[list1[i]]+=i
        for i in range(len(list2)):
            if list2[i] in hm:
                hm[list2[i]]+=i
        minval=min(hm.values())
        res=[key for key, value in hm.items() if value == minval]
       
        return res

