class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                summ = stack[-2] + stack[-1]
                stack.append(summ)
            elif op == "C":
                stack.pop()
            elif op == "D":
                val = stack[-1]
                stack.append(val*2)
            else:
                val = int(op)
                stack.append(val)
        return sum(stack)