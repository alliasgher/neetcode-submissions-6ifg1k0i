class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 2 pointer starting from middle of palindrome
        reslen = 0
        residx = 0
        
        for i, n in enumerate(s):
            l,r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    residx = l
                r+= 1
                l-= 1

        for i, n in enumerate(s):
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    residx = l
                r+= 1
                l-= 1
        
        return s[residx:residx+reslen]
        

            
        