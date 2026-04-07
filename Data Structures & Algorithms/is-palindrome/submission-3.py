class Solution:
    def isPalindrome(self, s: str) -> bool:
        # word = ""
        # for letter in s:
        #     if letter.isalnum():
        #         word += letter.lower()

        # print(word)

        # return word == word[::-1]

        #Sol using pointers
        l,r = 0, len(s) -1
        while l < r:

            if not self.isalphanumeric(s[l]):
                l+= 1
                continue
            if not self.isalphanumeric(s[r]):
                r-= 1
                continue

            print(s[l].lower())
            print(s[r].lower())

            if s[l].lower() != s[r].lower():
                return False
            l+= 1
            r-= 1

        return True


    def isalphanumeric(self, a: str):
        if (
            (ord('A') <= ord(a) <= ord('Z')) or
            (ord('a') <= ord(a) <= ord('z')) or
            (ord('0') <= ord(a) <= ord('9'))
        ):
            return True

        else:
            return False

        