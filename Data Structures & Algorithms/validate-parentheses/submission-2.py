class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mydict = {}

        mydict['{'] = '}'
        mydict['['] = ']'
        mydict['('] = ')'

        for i in range(len(s)):
            if s[i] in mydict:
                stack.append(s[i])
            else:
                if not stack:                # stack empty → no opening to match
                    return False
                last = stack.pop()
                if s[i] == mydict[last]:
                    continue
                else:
                    return False
        
        return len(stack) == 0
        