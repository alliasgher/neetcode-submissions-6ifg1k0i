class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def pal(word):
            l, r = 0, len(word)-1
            while l<= r:
                if word[l] != word[r]:
                    return False
                l+=1
                r-= 1
            return True

        def dfs(i):
            if i>= len(s):
                res.append(part.copy())

            for j in range(i, len(s)):
                curWord = s[i:j+1]
                if pal(curWord):
                    part.append(curWord)
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    


        