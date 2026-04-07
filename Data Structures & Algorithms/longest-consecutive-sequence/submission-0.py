class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        myset = set(nums)
        longest = 0

        for num in nums:
            current = 1
            if num-1 in myset:
                continue

            while num+1 in myset:
                current += 1
                num += 1

            longest = max(longest, current)

        return longest
        