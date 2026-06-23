class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if(i not in "+-*/"):
                stack.append(int(i))
            else:
                y=stack.pop()
                x=stack.pop()
                if i=="+":
                    stack.append(x+y)
                elif i=='-':
                    stack.append(x-y) 
                elif i=="*":
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
        return stack[-1] if stack else -1                  
            
