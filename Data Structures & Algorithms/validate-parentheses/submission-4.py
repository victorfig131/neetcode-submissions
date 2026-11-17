class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                removed = stack.pop()
                if removed != pairs[char]:
                    return False

        return not stack