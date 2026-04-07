class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre = [1] * len(nums)
        # post = [1] * len(nums)
        # res = []

        # for i, num in enumerate(nums):
        #     if i>0:
        #         pre[i] *= nums[i-1] * pre[i-1]
        #     else:
        #         pre[i] *= 1
        
        # for i in range(len(nums)-1, -1, -1):
        #     if i<len(nums)-1:
        #         post[i] *= nums[i+1] *post[i+1]
        #     else:
        #         post[i] *= 1
        #     print(post)

        # print(pre)
        # print(post)
        # for i, num in enumerate(nums):
        #     res.append(pre[i] * post[i])
        
        # return res

        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]

        pre = post = 1

        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]

        for i in range(len(nums) -1,-1,-1):
            postfix[i] = post
            post *= nums[i]
        
        for i in range(len(nums)):
            res[i] = postfix[i] * prefix[i]

        return res






        