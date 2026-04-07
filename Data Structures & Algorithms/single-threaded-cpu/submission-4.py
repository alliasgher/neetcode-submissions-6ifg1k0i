class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda t: t[0])
        time = 0
        minheap = []
        res = []
        i = 0
        n = len(tasks)


        while i<n or minheap:

            if not minheap and (time < tasks[i][0]):
                time = tasks[i][0]
            while (i<n and tasks[i][0] <= time):
                enqueue, proc, idx = tasks[i]
                heapq.heappush(minheap, (proc, idx, enqueue))
                i+= 1
            
            proc, ans, task = heapq.heappop(minheap)
            time += proc
            res.append(ans)
            
        return res
        

        
            

        
        