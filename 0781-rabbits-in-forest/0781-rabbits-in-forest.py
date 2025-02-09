class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        Rabitcounter=Counter(answers)
        res=0
        
        for key, count in Rabitcounter.items():
            size=key + 1
            num_groups=math.ceil(count/size)
            res+=size * num_groups
        
        return res