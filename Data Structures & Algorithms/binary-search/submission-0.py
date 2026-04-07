class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            print(nums[l:r+1])
            
            mid = (l+r) // 2
            print(nums[mid])

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid-1

            elif nums[mid] < target:
                l = mid+1
            

        return -1
        