class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        nxt = 1
        nxt1 = 1

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                tmp = 0
            else:
                tmp = nxt

            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                tmp += nxt1 
            
            nxt, nxt1 = tmp, nxt

            
            
        return nxt


        