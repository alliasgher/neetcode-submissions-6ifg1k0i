class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l = 0
        res = 0
        prod = 1

        for r, num in enumerate(nums):
            prod *= num

            while prod >= k and l<=r:
                prod //= nums[l]
                l+= 1

            res += r-l+1

        return res

        