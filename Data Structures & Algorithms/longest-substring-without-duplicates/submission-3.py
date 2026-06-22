class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        lens=0
        letters=set()
        while(l<=r and r<len(s)):
            
            if(s[r] not in letters):
                letters.add(s[r])
            else:
                while(s[r] in letters and l<=r):
                    letters.remove(s[l])
                    l+=1
                letters.add(s[r])
            lens=max(lens,r-l+1)
            r+=1
        return lens