class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) - 1
        maxi = 0

        while l<r:
            area = abs(l-r) * min(heights[l], heights[r])
            print(heights[l], heights[r],area)
            maxi = max(maxi, area)

            if heights[l]>heights[r]:
                r -= 1
            else:
                l+= 1
        
        return maxi


        