class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(0)
            elif c == "{":
                stack.append(1)
            elif c == "[":
                stack.append(2)
            elif c == ")":
                if (not stack) or stack[-1] != 0:
                    return False
                stack.pop()
            elif c == "}":
                if (not stack) or stack[-1] != 1:
                    return False
                stack.pop()
            else:
                if (not stack) or stack[-1] != 2:
                    return False
                stack.pop()
        return not stack
