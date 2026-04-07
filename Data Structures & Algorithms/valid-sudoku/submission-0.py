class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Instead of defaultdict(set)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Check row, column, and 3x3 box
                if val in rows[r] or val in cols[c] or val in squares[r // 3][c // 3]:
                    return False

                # Add value to the corresponding sets
                rows[r].add(val)
                cols[c].add(val)
                squares[r // 3][c // 3].add(val)

        return True
