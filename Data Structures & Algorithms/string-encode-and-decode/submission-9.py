class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for word in strs:
            newstr += str(len(word)) + '/' + word
        print(newstr)
        return newstr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i< len(s):
            j = i
            while s[j] != '/':
                j += 1
            num = int(s[i:j])
            res.append(s[j+1:j+1+num])
            i = j+1+num
        return res

