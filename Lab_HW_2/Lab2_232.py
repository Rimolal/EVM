class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[0]
        self.stack = self.stack[1:]
        return x

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


obj = MyQueue()
    
obj.push(1)
obj.push(2)
obj.push(3)
    
print(f"peek: {obj.peek()}")
print(f"pop: {obj.pop()}")
print(f"empty: {obj.empty()}")
print(f"pop: {obj.pop()}")
print(f"pop: {obj.pop()}")
print(f"empty: {obj.empty()}")