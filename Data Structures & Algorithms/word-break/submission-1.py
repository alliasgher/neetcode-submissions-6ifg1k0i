class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        found = {}
        found[len(s)] = True

        def dfs(i):
            if i in found:
                return found[i]
            
            found[i] = False
            
            for word in wordDict:
                wordlen = len(word)

                if i+wordlen <= len(s) and s[i:i+wordlen] == word:
                    found[i] = dfs(i+wordlen)
            
                if found[i]:
                    return True
            
            return False
        
        return dfs(0)



        