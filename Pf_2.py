class Counter():
    def __init__(self) -> None:
        self.value=0
        self.history=[self.value]
    
    def increment(self):
        self.value += 1
        self.history.append(self.value)
        return self.value
    
    def get_values(self):
        return self.value
    
    def decrement(self):
        self.value -= 1
        self.history.append(self.value)
        return self.value
    
    def reset(self):
        self.value=0
        self.history.append(self.value)
        return self.value
    def set_value(self, x: int):
        self.value=x
        self.history.append(self.value)
        return self.value
    def get_history(self):
        return self.history







c=Counter()
print(c.get_values())
print(c.increment())
print(c.increment())
print(c.get_values())
print(c.decrement())
print(c.increment())
print(c.increment())
print(c.decrement())
print(c.reset())
print(c.set_value(21))
print(c.get_values())
print(c.get_history())
