class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        summ = 0

        def dfs(i):
            nonlocal summ
            if summ == target:
                res.append(subset.copy())
                return

            if i == len(nums) or summ > target:
                return

            subset.append(nums[i])
            summ += nums[i]
            dfs(i)

            subset.pop()
            summ -= nums[i]
            dfs(i+1)

        dfs(0)
        return res
        