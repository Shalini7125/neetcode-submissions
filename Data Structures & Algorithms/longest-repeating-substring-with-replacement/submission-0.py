class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=right=0
        n=len(s)
        unique=[0]*26
        maxcount=0
        while right<n:
            unique[ord(s[right])-65]+=1
            while(right-left+1-max(unique) >k):
                unique[ord(s[left])-65]-=1
                left+=1
            maxcount=max(maxcount,right-left+1)
            right+=1
        return maxcount
        