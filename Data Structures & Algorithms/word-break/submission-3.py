class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # found = {}
        # found[len(s)] = True

        # def dfs(i):
        #     if i in found:
        #         return found[i]
            
        #     found[i] = False
            
        #     for word in wordDict:
        #         wordlen = len(word)

        #         if i+wordlen <= len(s) and s[i:i+wordlen] == word:
        #             found[i] = dfs(i+wordlen)
            
        #             if found[i]:
        #                 return True
            
        #     return False
        
        # return dfs(0)

        found = [False] * (len(s)+1)
        found[len(s)] = True


        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                wordlen = len(word)

                if i+wordlen <= len(s) and s[i:i+wordlen] == word:
                    found[i] = found[i+wordlen]

                    if found[i]:
                        break
        
        return found[0]



        