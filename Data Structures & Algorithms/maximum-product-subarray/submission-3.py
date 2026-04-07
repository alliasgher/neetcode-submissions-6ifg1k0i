class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = nums[0]

        for num in nums:
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp * num, curMin * num, num)
            res = max(res, curMax)
        return res


        # for n in nums:
        #     if n<0:
        #         tmp = curMin
        #         curMin = min(curMax*n, n)
        #         curMax = max(tmp*n, n)
        #     else:
        #         curMin = min(curMin*n, n)
        #         curMax = max(curMax*n, n)
        #     res = max(curMax, res)

        # return res


        
        