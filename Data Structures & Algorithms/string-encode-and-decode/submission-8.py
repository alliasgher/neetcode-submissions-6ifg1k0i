class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ""
        for word in strs:
            newstr += str(len(word)) + '/' + word
        print(newstr)
        return newstr

    def decode(self, s: str) -> List[str]:
        res = []
        length = len(s)
        while length >0:
            num = ""
            while s[0] != "/":
                num += s[0]
                s = s[1:]
            num = int(num)
            print("num: ", num)
            s = s[1:]
            res.append(s[:num])
            print('word: ', s[:num])
            s = s[num:]
            length = len(s)
        return res

