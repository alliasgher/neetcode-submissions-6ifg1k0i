class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if total > target or i == len(candidates):
                return

            subset.append(candidates[i])
            total += candidates[i]
            dfs(i+1, subset, total)

            #not include
            subset.pop()
            total -= candidates[i]
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return res


        