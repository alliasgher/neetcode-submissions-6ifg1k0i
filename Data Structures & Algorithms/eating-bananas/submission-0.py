class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        res = 0

        l, r = 1, k

        while l<=r:
            m = (l+r) // 2
            print(m)
            total = 0
            for pile in piles:
                total += (pile+m-1)//m

            if total <= h:
                res = m
                r = m-1
            elif total > h:
                l = m+1
            print(total, l, r)
            
        return res

        