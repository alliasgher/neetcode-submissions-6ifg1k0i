class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = {}
        heap = []
        time = 0

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        for _, value in count.items():
            heap.append(-value)

        heapq.heapify(heap)

        q = deque()

        while heap or q:
            time += 1

            if heap:
                curr = heapq.heappop(heap)
                if curr+1 != 0:
                    q.append([curr+1, time+n]) #+1 due to rev heap

            while q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(heap, count)

        return time
            
        