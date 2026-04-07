class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda t: t[0])
        time = tasks[0][0]
        minheap = []
        res = []


        while tasks or minheap:
            while (tasks and tasks[0][0] <= time) or not minheap:
                heapq.heappush(minheap, (tasks[0][1], tasks[0][0], tasks[0][2]))
                tasks = tasks[1:]
            
            proc, task, i = heapq.heappop(minheap)
            time += proc
            res.append(i)
            print(tasks)
            print("task: ", task, proc)

            

            
        return res
        

        
            

        
        