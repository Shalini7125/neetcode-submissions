from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lens=0
        maxf=0
        l,r=0,0
        count=defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            maxf=max(maxf,count[s[r]])
            while(r-l+1-maxf>k):
                count[s[l]]-=1
                l+=1
            lens=max(lens,r-l+1)
        return lens


        