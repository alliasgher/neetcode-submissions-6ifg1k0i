class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # rows, cols = len(grid), len(grid[0])

        # directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # res = 0

        # def dfs(r, c):
        #     grid[r][c] = "0"
        #     stack = []
        #     stack.append((r,c))

        #     while stack:
        #         r,c = stack.pop()
                
        #         for d in directions:
        #             dr, dc = d
        #             dr = r+dr
        #             dc = c+dc
        #             if (dr<0 or dc<0 or dr>= rows or dc>= cols or 
        #             grid[dr][dc] == "0"):
        #                 continue
        #             stack.append((dr,dc))
        #             grid[dr][dc] = "0"


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r,c)
        #             res += 1
        
        # return res























        rows, cols = len(grid), len(grid[0])

        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def dfs(r,c):
            if  0>r or r>=rows or 0>c or c>=cols or grid[r][c] == '0':
                return
            
            
            for dirn in dirs:
                row, col = dirn
                dfs(r+row, c+col)
                grid[r][c] = '0'
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)    
                    res += 1

        return res

        

