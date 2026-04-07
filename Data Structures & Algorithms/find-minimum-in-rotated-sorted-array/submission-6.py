class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums)-1

        # while l<r:
        #     m = (l+r) // 2
        #     if nums[m] > nums[r]:
        #         l = m+1
        #     else:
        #         r = m
        
        # return nums[l]

        res = 1000

        l, r = 0, len(nums) -1

        while l<=r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            m = (l+r) // 2
            print(nums[l], nums[m], nums[r])
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        
        return res


        


        