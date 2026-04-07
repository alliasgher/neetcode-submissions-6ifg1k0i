class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        

        while len(s) > 0:
            i = 0
            while s[i+1] != "#":
                i += 1
            
            length = int(s[0:i+1])
            print("length", length)
            print("i", i)

            res.append(s[i+2:i+2 + length])
            s = s[i+2+length:]
            print("res", res)
            print("s", s)

        return res

