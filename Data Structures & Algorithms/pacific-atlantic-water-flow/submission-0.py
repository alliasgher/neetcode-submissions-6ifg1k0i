class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific, atlantic = set(), set()

        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c, myset):
            if (r,c) in myset:
                return
            myset.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, myset)



        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        res = []

        for (x,y) in pacific:
            if (x,y) in atlantic:
                res.append([x,y])

        return res


        
        