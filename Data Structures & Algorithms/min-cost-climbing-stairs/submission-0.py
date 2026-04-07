class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        reach = 1

        top = len(cost)

        dp = [0] * (top+1)

        for i in range(top-1, -1, -1):
            if i == top-1:
                dp[i] = cost[i]

            elif i == top-2:
                dp[i] = min(cost[i], cost[i] + dp[i+1])

            else:
                dp[i] =  min(cost[i] + dp[i+2], cost[i] + dp[i+1])
            print(i+1, dp[i])

        return min(dp[0], dp[1])

        
        