class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mydict = {}

        for word in strs:
            mylist = [0] * 26
            for letter in word:
                mylist[ord(letter) - ord('a')] += 1

            key = tuple(mylist)

            if key not in mydict:
                mydict[key] = []

            mydict[key].append(word)

        return list(mydict.values())

        
        