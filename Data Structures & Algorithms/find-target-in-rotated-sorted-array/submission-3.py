class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r) // 2
            print(nums[l:m+1], nums[m+1:r+1])

            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                #left sorted
                #only use = with r, l as we are alr checking for m at start
                if nums[m] > target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                #right sorted
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            
        if target == nums[l]:
            return l
        return -1

                
        