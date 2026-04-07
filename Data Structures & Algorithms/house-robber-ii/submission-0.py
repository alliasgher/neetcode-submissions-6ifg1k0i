class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob2(nums):
            first, second = 0, 0

            for n in nums:
                tmp = max(first+n, second)
                first = second
                second = tmp
            return second

        return max(rob2(nums[:-1]), rob2(nums[1:]))
        