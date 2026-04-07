class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        # cost.append(0) 
        # for i in range(len(cost)-3, -1, -1): 
        #     cost[i] = min(cost[i] + cost[i+2], cost[i] + cost[i+1]) 
            
        # return min(cost[0], cost[1])

        
        last = 0
        second = cost[-1]

        #ignore last 2 indexes
        for i in range(len(cost)-2, -1, -1):
            tmp =  min(cost[i] + last, cost[i] + second)
            last = second
            second = tmp


        return min(last, second)

        
        