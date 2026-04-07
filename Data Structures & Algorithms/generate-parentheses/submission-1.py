class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(cur, openn, close):
            if openn == n  and close == n:
                res.append(cur)
                return

            if openn < n :
                dfs(cur + '(', openn+1, close)

            if close < openn:
                dfs(cur + ')', openn, close+1)



        dfs("", 0, 0)
        return res

        