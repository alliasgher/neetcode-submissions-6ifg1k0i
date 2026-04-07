class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        path = set()

        def dfs(r,c, curWord):
            if len(curWord) == 0:
                return True

            if (r< 0 or c<0 or r== rows or c== cols or 
            curWord[0] != board[r][c] or (r,c) in path):
                return False

            path.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if dfs(nr, nc, curWord[1:]):
                    return True
            path.remove((r,c))
            return False



        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, word):
                    return True

        return False
        