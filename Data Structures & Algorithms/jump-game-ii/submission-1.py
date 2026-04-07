class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        dp[len(nums)-1] = 0

        for i in range(len(nums)-2,-1,-1):
            x = nums[i]
            res = float("inf")
            for j in range(x):
                if i+j+1 <= len(nums)-1:
                    cur = 1 + dp[i+j+1]
                    res = min(res,cur)
            
            dp[i] = res
        
        return dp[0]



        