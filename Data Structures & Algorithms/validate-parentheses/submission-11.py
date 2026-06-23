class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if(i in "([{"):
                stack.append(i)
            else:
                if(stack and stack[-1]==mapping[i]):
                    stack.pop()
                    
                else:return False
                
        if(len(stack)==0):return True
        else:return False
                    


        