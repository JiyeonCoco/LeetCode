class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for c in s[::-1]:

            if c in ')}]':
                stack.append(c)

            else:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
