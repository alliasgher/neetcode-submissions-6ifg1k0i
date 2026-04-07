class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers
        # l,r = 0,1
        # highest=0
        # while r < len(prices):
        #     current = prices[r] - prices[l]
        #     highest = max(highest, current)
        #     print(highest)

        #     if prices[r] < prices[l]:
        #         l = r
        #         r = l+1
        #         continue

        #     r+= 1

        # return highest


        #dynamic

        mini = prices[0]
        highest = 0

        for price in prices:
            highest = max(highest, price-mini)
            mini = min(mini, price)
        
        return highest