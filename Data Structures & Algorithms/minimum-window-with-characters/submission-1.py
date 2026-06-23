class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt={}
        window={}
        result=(-1,-1)
        res=float("inf")
        
        for i in t:
            countt[i]=countt.get(i,0)+1
        left,right=0,0
        have,need=0,len(countt)
        while(left<len(s)):
            window[s[left]]=window.get(s[left],0)+1
            if(s[left] in countt and countt[s[left]]==window[s[left]]):
                have+=1
            while(need==have): 
                if(left-right+1<res):
                    result=(right,left)
                    res=left-right+1
                window[s[right]]-=1
                if(s[right] in countt and window[s[right]]<countt[s[right]]):
                    have-=1
                right+=1
            left+=1
        return s[result[0]:result[1]+1] if res!=float('inf') else ''






        