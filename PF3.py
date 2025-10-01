class Stack:
    def __init__(self) -> None:
        self.stack=[]
        self.min_stack=[]
        self.max_stack=[]
    
    def push(self, value)-> int:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        return len(self.stack)
    
    def pop(self)-> int | None:
        if not self.stack:
            return None
        val=self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val
    
    def peek(self)-> int | None:
        if not self.stack:
            return None
        return self.stack[-1]
    def is_empty(self) ->bool:
        return not self.stack
    def size(self) -> int:
        return len(self.stack)
    def get_min(self) -> int| None:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    def get_max(self) -> int | None:
        if not self.max_stack:
            return None
        return self.max_stack[-1]


    
s=Stack()
print(s.pop())
print(s.peek())
print(s.push(2))
print(s.push(5))
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())
print(s.pop())
print(s.size())
print(s.is_empty())
print(s.get_min())
print(s.pop())
print(s.pop())
print(s.get_min())
print(s.get_max())
print(s.push(50))
