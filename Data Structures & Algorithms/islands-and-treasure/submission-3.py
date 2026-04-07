class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #can be done with or without set
        visited = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        # def bfs(r,c):
        #     if (r not in range(rows) or c not in range(cols) or 
        #     (r,c) in visited or grid[r][c] == -1 or grid[r][c] == 0):
        #         return
            
        #     q.append((r,c))
        #     visited.add((r,c))

        def bfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == -1 or
                grid[r][c] <= dist
            ):
                return

            grid[r][c] = dist + 1   # 🔑 mark visited here
            q.append((r, c))

            
            


        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                

                for dr,dc in dirs:
                    nr, nc = r + dr, c + dc
                    bfs(nr,nc)
            dist += 1
        
                    

                

        