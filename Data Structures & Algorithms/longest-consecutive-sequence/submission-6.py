class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        if(len(nums)==0):
            return 0
        max1=1
        for i in nums:
            if(i-1 in n):
                continue
            x=i+1
            while(x in n):
                max1=max(max1,x-i+1)
                x+=1
        return max1
            
        