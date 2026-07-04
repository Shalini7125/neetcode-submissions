class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for coin in coins:
            for s in range(coin,amount+1):
                dp[s]=min(dp[s],dp[s-coin]+1)
        return dp[amount] if dp[amount]<=amount else -1
        