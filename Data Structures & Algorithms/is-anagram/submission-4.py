class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for letter in s:
            dict1[letter] = dict1.get(letter, 0)+1

        for letter in t:
            dict1[letter] = dict1.get(letter, 0)-1

        for value in dict1.values():
            if value!= 0:
                return False
        return True
        