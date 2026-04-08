class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        dic = {}
        maxf = 0

        for r in range(len(s)):
            cur = s[r]
            dic[cur] = dic.get(cur, 0) + 1
            maxf = max(maxf, dic[cur])
            
            while (r-l+1) - maxf > k:
                dic[s[l]] = dic.get(s[l], 0) - 1
                l+= 1
            res = max(r-l+1, res)
            
            

        return res
            


                


            
                

        