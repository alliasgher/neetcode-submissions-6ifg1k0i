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
        q = deque()
        res = []

        for r in range(len(nums)):
            
            while len(q) > 0 and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if r >= k-1:
                while q and q[0] < l:
                    q.popleft()

                res.append(nums[q[0]])
                l += 1
        
        return res



        