class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        res = []

        for word in strs:
            letters = [0 for i in range(26)]
            for letter in word:
                key = ord(letter) - ord('a')
                letters[key] += 1
            letters = tuple(letters)
            mydict[letters] = mydict.get(letters, [])
            mydict[letters].append(word)

        for arr in mydict.values():
            res.append(arr)

        return res

        # mydict = {}
        # res = []

        # for word in strs:
        #     myarr = [0]*26
        #     for letter in word:
        #         myarr[ord(letter) - ord('a')] += 1
        #     key = tuple(myarr)
        #     if key not in mydict:
        #         mydict[key] = []
        #     mydict[key].append(word)
        # for key, value in mydict.items():
        #     res.append(value)
        # return res


        
                
        