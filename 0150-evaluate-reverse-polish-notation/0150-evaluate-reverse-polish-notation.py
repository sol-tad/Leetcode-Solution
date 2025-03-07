class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for opr in tokens:
            if opr.lstrip('-').isdigit():
                stack.append(opr)
            else:
                num2=int(stack.pop())
                num1=int(stack.pop())
                res=0
                if opr=='+':
                    res=num1 + num2
                elif opr=='-':
                    res=num1 - num2
                elif opr=='/':
                    res=int(num1/num2)
                elif opr=='*':
                    res=num1 *num2
                stack.append(res)
            print(stack)
        return int(stack[0])