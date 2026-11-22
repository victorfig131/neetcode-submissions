class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x = stack.pop()
                y = stack.pop()
                result = x + y
                stack.append(result)
            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                result = x * y
                stack.append(result)
            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                result = y - x
                stack.append(result)
            elif i == "/":
                x = stack.pop()
                y = stack.pop()
                result = y/x
                stack.append(int(result))
            else:
                stack.append(int(i))
        return stack[-1]