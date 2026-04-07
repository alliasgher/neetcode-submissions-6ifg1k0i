class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False

        # dict1 = {}
        # dict2 = {}

        # for i in range(len(s1)):
        #     dict1[s1[i]] = dict1.get(s1[i], 0) +1
        #     dict2[s2[i]] = dict2.get(s2[i], 0) +1

        # l = matches = 0
        # for r in range(len(s1), len(s2)):
        #     if dict1 == dict2:
        #         return True
            
        #     dict2[s2[r]] = dict2.get(s2[r], 0) + 1
        #     dict2[s2[l]] = dict2[s2[l]] - 1
        #     if dict2[s2[l]] == 0:
        #         del dict2[s2[l]]
        #     l+= 1

        # return dict1==dict2

        count1 = [0] * 26
        count2 = [0] * 26

        l = matches = 0
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            
            letter = ord(s2[r]) - ord('a')
            count2[letter] += 1
            if count2[letter] == count1[letter]:
                matches += 1
            if count2[letter] - 1 == count1[letter]:
                matches -= 1

            letter = ord(s2[l]) - ord('a')
            count2[letter] -= 1
            if count2[letter] == count1[letter]:
                matches += 1
            if count2[letter] + 1 == count1[letter]:
                matches -= 1

            l+= 1

        return matches == 26




        