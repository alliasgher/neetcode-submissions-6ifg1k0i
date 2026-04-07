class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        ans = 0

        l = r = 0

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l+= 1
            myset.add(s[r])
            ans = max(ans, len(myset))

        return ans




        