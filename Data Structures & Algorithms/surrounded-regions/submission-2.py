class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r,c):
            board[r][c] = "2"
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if not ( 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O"):
                    continue
                
                dfs(nr,nc)


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r== rows-1 or c == 0 or c == cols-1:
                    if board[r][c] == "O":
                        
                        dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "2":
                    board[r][c] = "O"

                

        