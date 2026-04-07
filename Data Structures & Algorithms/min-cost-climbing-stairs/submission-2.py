class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        last = 0
        second = cost[-1]

        #ignore last 2 indexes
        for i in range(len(cost)-2, -1, -1):
            tmp =  min(cost[i] + last, cost[i] + second)
            last = second
            second = tmp


        return min(last, second)

        
        