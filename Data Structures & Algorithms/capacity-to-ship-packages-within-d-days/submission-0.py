class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        maxk, sumk = max(weights), sum(weights)
        res = sumk
        l, r = maxk, sumk

        def canship(cap):
            days = 1
            curcap = cap
            for weight in weights:
                if curcap - weight < 0:
                    days += 1
                    curcap = cap
                curcap -= weight
            return days
        
        while l<=r:
            m = (l+r) // 2
            x = canship(m)
            if x<=days:
                res = m
                r = m-1
            else:
                l = m+1
        return res

        



        