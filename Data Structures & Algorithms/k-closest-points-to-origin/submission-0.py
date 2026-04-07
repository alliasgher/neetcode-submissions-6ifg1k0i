class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minheap = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x ** 2) + (y ** 2)
            minheap.append([dist, x, y])


        #python compares lexographically
        heapq.heapify(minheap)

        while k>0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -= 1

        return res

        