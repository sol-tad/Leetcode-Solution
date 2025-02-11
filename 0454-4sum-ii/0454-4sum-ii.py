class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hmnums1_nums2=defaultdict(int)
        for n in nums1:
            for n1 in nums2:
                hmnums1_nums2[n+n1]+=1
        count=0

        for n in nums3:
            for n1 in nums4:
                if hmnums1_nums2[-(n+n1)]:
                    count+=hmnums1_nums2[-(n+n1)]
        return count