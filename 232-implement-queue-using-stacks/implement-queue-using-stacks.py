class MyQueue:

    def __init__(self):
        self.stack = []
        self.invertedStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return
        

    def pop(self) -> int:
        if self.invertedStack:
            return self.invertedStack.pop()
        while self.stack:
            self.invertedStack.append(self.stack.pop())
        return self.invertedStack.pop()

    def peek(self) -> int:
        if self.invertedStack:
            return self.invertedStack[-1]
        while self.stack:
            self.invertedStack.append(self.stack.pop())
        return self.invertedStack[-1]

    def empty(self) -> bool:
        if self.invertedStack or self.stack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()