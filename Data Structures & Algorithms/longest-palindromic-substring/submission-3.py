class Solution:
    def longestPalindrome(self, s: str) -> str:

        # # 2 pointer starting from middle of palindrome
        reslen = 0
        residx = 0
        
        # #for odd palindromes
        # for i, n in enumerate(s):
        #     l,r = i, i
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         if r-l+1 > reslen:
        #             reslen = r-l+1
        #             residx = l
        #         r+= 1
        #         l-= 1

        # #for even length palindromes:
        # for i, n in enumerate(s):
        #     l,r = i, i+1
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         if r-l+1 > reslen:
        #             reslen = r-l+1
        #             residx = l
        #         r+= 1
        #         l-= 1
        
        # return s[residx:residx+reslen]

        #dynamic
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        #start i in reverse because we need to check dp[i+1][j-1]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j-i <= 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > reslen:
                        reslen = j-i+1
                        residx = i

        return s[residx:residx+reslen]

            




        

            
        