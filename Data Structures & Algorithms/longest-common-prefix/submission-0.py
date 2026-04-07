class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        n = 1000000
        for word in strs:
            n = min(n, len(word))

        for i in range(n):
            cur = ""
            for word in strs:
                if not cur:
                    cur = word[i]
                if word[i] != cur:
                    return res
            res += cur

        return res



        

        