class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0


        #dynamic
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        #start i in reverse because we need to check dp[i+1][j-1]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j-i <= 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1

        return res
        

        #odd length
        # for i in range(len(s)):
        #     l, r = i, i

        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r+= 1

        # #even length
        # for i in range(len(s)):
        #     l, r = i, i+1

        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r+= 1
        
        # return res

        
        