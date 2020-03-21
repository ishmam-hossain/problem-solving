class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 99999999999999

    def push(self, x: int) -> None:
        self.min = min(x, self.min)
        self.stack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            self.min = min(self.stack) if self.stack else 99999999999999
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
