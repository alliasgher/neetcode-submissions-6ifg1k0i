class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(cur, openn, close):
            if openn == n  and close == n:
                res.append(cur)
                return

            if openn < n and close < openn:
                dfs(cur + '(', openn+1, close)

                dfs(cur + ')', openn, close+1)
            
            elif openn < n and close == openn:
                dfs(cur + '(', openn+1, close)

            elif openn == n and close < openn:
                dfs(cur + ')', openn, close+1)
            
            else:
                return


        dfs("", 0, 0)
        return res

        