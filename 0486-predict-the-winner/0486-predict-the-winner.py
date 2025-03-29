class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(left, right):
            if left==right:
                return nums[left]
            ChooseLeft = nums[left]-score(left + 1,right)
            ChooseRight = nums[right]-score(left,right-1)
            return max(ChooseLeft,ChooseRight)

        return score(0, len(nums) - 1) >= 0
