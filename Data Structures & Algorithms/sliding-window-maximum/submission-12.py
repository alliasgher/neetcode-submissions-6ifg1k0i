class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # l = r = 0
        # q = deque() #keep only index 
        # res = []

        # for r in range(len(nums)):
            
        #     while len(q) > 0 and nums[r] > nums[q[-1]]:
        #         q.pop() #only decreasing order

        #     q.append(r)

        #     while q and q[0] < l:
        #         q.popleft() #first value less than acceptable left most index

        #     if r >= k-1:

        #         res.append(nums[q[0]])
        #         l += 1
        
        # return res


        #heap
        l = 0
        heap = [] #(-value, index) 
        res = []

        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] < l:
                heapq.heappop(heap)

            if r >= k-1:
                res.append(-heap[0][0])
                l += 1
        
        return res








        