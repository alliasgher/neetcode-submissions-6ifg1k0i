class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        left,right = -1, -1

        def searchLeft():
            nonlocal left
            l, r = 0, len(nums) - 1
            while l<=r:
                m = (l+r) // 2
                if nums[m] == target:
                    left = m
                    r = m-1
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        
        def searchright():
            nonlocal right
            l, r = 0, len(nums) - 1
            while l<=r:
                m = (l+r) // 2
                if nums[m] == target:
                    right = m
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
                
        
        searchLeft()
        searchright()

        return [left,right]
            
        