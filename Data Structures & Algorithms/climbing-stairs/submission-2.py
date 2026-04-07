class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = [0 for _ in range(n+1)]

        # if n == 1:
        #     return 1
        
        # if n == 2:
        #     return 2

        # dp[1], dp[2] = 1,2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[-1]

        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one+two
            two = temp

        return one



        