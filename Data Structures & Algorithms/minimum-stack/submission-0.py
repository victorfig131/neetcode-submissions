class MinStack:

    def __init__(self):
        self.stack = []
        self.prevmin = []
        self.min = 2**31

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prevmin.append(self.min)
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.prevmin.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
