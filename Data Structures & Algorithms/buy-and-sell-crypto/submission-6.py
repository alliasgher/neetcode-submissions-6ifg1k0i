class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointers
        # l,r = 0,1
        # maxp = 0

        # while r < len(prices):
        #     profit = prices[r] - prices[l]
        #     maxp = max(maxp, profit)

        #     if prices[r] < prices[l]:
        #         l = r
        #     r+= 1
        
        # return maxp


        #dynamic
        minbuy = prices[0]
        maxp = 0

        for i in range(1, len(prices)):
            maxp = max(prices[i] - minbuy, maxp)
            minbuy = min(minbuy, prices[i])

        return maxp



        