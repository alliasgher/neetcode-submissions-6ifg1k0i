class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        # dp = {0:0}
        # INF = float("inf")

        # def dfs(a):

        #     if a in dp:
        #         return dp[a]

        #     best = INF
        #     for c in coins:
        #         if a - c >= 0:
        #             best = min(best, 1+ dfs(a-c))
            
        #     dp[a] = best
        #     return best
        
        # ans = dfs(amount)
        # return -1 if ans == INF else ans


        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for a in range(amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1+ dp[a-coin])

        return dp[amount] if dp[amount] != float("inf") else -1

        

        
                    