class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=nums
        if(len(nums)<=2):
            return max(nums)
        dp[2]=max(dp[1],dp[0]+dp[2])
        for i in range(3,len(nums)):
            dp[i]=max(dp[i-1],dp[i]+dp[i-2],dp[i]+dp[i-3])
        return max(dp[-1],dp[-2])

        