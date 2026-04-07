class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) -1

        while l<r:
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r-l) // 2
            print(nums[l:r+1])
            if nums[m] > nums[r]:
                print("doing l=m+1")
                l = m +1
            else:
                print("doing r=m")
                r = m

        return nums[l]
        


        