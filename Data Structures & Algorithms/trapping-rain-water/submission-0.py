class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxL = height[l]
        maxR = height[r]
        res = 0

        while l<r:
            if maxL > maxR:
                r -= 1
                curr = min(maxL, maxR) - height[r]
                if curr > 0:
                    res += curr
                maxR = max(maxR, height[r])
                

            else:
                l+= 1
                curr = min(maxL, maxR) - height[l]
                if curr > 0:
                    res += curr
                maxL = max(maxL, height[l])
        return res

        