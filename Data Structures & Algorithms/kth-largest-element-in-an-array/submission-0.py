class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        heap = [-num for num in nums]

        heapq.heapify(heap)

        while k>1:
            heapq.heappop(heap)
            k -=1

        res = -heapq.heappop(heap)

        return res

        