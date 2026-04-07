class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                tmp = nums[i]
                nums[i] = nums[l]
                nums[l] = tmp
                l+= 1
                i += 1
            elif nums[i] == 2:
                tmp = nums[i]
                nums[i] = nums[r]
                nums[r] = tmp
                r -= 1
            else:
                i += 1
        
        return nums
            
        