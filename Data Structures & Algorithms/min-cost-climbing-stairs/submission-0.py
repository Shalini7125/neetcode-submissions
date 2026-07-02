class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=cost
        n=len(cost)
        if(n<=2):return min(cost)
        for i in range(2,n):
            dp[i]=min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        return min(dp[-1],dp[-2])
        