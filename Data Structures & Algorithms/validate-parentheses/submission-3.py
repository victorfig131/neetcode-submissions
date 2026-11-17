class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2: return False

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char == ')' and stack:
                removed = stack.pop()
                if removed != '(':
                    return False
            elif char == ']' and stack:
                removed = stack.pop()
                if removed != '[':
                    return False
            elif char == '}' and stack:
                removed = stack.pop()
                if removed != '{':
                    return False
            elif not stack:
                return False
        if stack: return False
        return True