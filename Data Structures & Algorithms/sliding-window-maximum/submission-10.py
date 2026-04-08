class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # l = r =0
        # q = deque()
        # res = []

        # while r < len(nums):
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     if l > q[0]:
        #         q.popleft()

        #     if r+1>=k:
        #         res.append(nums[q[0]])
        #         l+= 1
        #     r+= 1

        # return res













        l = r = 0
        q = deque() #keep only index 
        res = []

        for r in range(len(nums)):
            
            while len(q) > 0 and nums[r] > nums[q[-1]]:
                q.pop() #only decreasing order

            q.append(r)

            while q and q[0] < l:
                q.popleft() #first value less than acceptable left most index

            if r >= k-1:

                res.append(nums[q[0]])
                l += 1
        
        return res



        