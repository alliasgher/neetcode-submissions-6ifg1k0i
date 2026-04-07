class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        # def dfs(r,c):
        #     if  0>r or r>=rows or 0>c or c>=cols or grid[r][c] == 0:
        #         return 0
            
        #     temp = 1
        #     grid[r][c] = 0 #MARK VISITED IMMEDIATELY
            
        #     for dirn in dirs:
        #         row, col = dirn
        #         temp += dfs(r+row, c+col) 

        #     return temp
                

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             res = max(dfs(r,c), res)   

        # return res

        stack = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    stack.append((r,c))
                    grid[r][c] = 0
                    area = 0

                    while stack:
                        cr, cc = stack.pop()
                        area += 1

                        for dr, dc in dirs:
                            nr, nc = cr+dr, cc+dc
                            if 0<=nr< rows and 0<=nc< cols and grid[nr][nc] == 1:
                                stack.append((nr,nc))
                                grid[nr][nc] = 0

                    res = max(res, area)

        return res
