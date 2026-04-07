class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Prepare keys
                square_key = (r // 3, c // 3)

                # Get or initialize sets
                rows[r] = rows.get(r, set())
                cols[c] = cols.get(c, set())
                squares[square_key] = squares.get(square_key, set())

                # Check for duplicates
                if val in rows[r] or val in cols[c] or val in squares[square_key]:
                    return False

                # Add the value
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        return True
