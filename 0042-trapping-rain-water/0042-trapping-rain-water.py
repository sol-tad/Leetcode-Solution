class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            if not stk:
                stk.append((i, height[i]))
            else:
                
                index , temp = stk[-1]
                while stk and len(stk) > 1 and temp <=  height[i]:
                    newind , newtemp = stk.pop()
                    index , temp = stk[-1]
                    res += (min(temp , height[i]) - newtemp) * (i - index - 1)

                while stk and stk[-1][1]< height[i]:
                    stk.pop()
                
                stk.append((i, height[i]))
        print(stk)
        return res
