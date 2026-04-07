class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[-1] = True

        for i in range(len(nums)-2, -1,-1):
            print(dp)
            if nums[i] == 0:
                continue
            x = nums[i]
            for j in range(x):
                if dp[i+j+1]:
                    dp[i] = True
                    break
        
        return dp[0]
            

        



        