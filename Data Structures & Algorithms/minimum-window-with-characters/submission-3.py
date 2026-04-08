class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        matches = 0
        tdict = {}
        sdict = {}
        inf = float("inf")
        resLen = inf
        res = [0,0]

        for i in range(len(t)):
            tdict[t[i]] = 1 + tdict.get(t[i], 0)
        req = len(tdict)


        for r in range(len(s)):
            curr = s[r]
            
            if curr in tdict:
                sdict[curr] = 1 + sdict.get(curr, 0)
                if tdict[curr] == sdict[curr]:
                    matches += 1
            
            while matches == req:
                
                curr = s[l]
                if (r-l+1) < resLen:
                    res = [l,r]
                resLen = min(resLen, r-l+1)
                if curr in tdict:
                    sdict[curr] -= 1
                if curr in tdict and sdict[curr] < tdict[curr]:
                    matches-= 1
                l+= 1
        if resLen == inf:
            return ""
        else:
            return s[res[0]:res[1]+1]




        
        