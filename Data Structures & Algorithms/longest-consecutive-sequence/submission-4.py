class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0

        for num in nums:
            if num-1 in myset:
                continue
            else:
                length = 1
                while (num+length) in myset:
                    length += 1
            longest = max(longest, length)
        return longest


        