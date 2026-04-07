class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i,num in enumerate(nums):
            if num <= 0 or num>n:
                nums[i] = n+1
        
        print(nums)
        for i,num in enumerate(nums):
            x = abs(num)
            if x == n+1:
                continue
            if nums[x-1] < 0:
                continue
            nums[x-1] *= -1
        
        for i,num in enumerate(nums):
            if num>0:
                return i+1

        return n+1
            

        