class BankAccount:
    def __init__(self) -> None:
        self.balance=0
        self.history=[]
    def deposit(self, amount: int) ->int:
        self.balance +=amount
        self.history.append(("deposit", amount))
        return self.balance
    def withdraw(self, amount: int) -> bool:
        if self. balance >= amount:
            self.balance -= amount
            self.history.append(("withdraw", amount))
            return True
        return False
    def get_balance(self) -> int:
        return self.balance
    def get_history(self) -> list[tuple[str, int]]:
        return self.history
    
    def undo(self) -> bool:
        if not self.history:
            return False
        last_action, amount=self.history.pop()
        if last_action=="deposit":
            self.balance -= amount
        elif last_action == "withdraw":
            self.balance += amount
        
        return True

    def transfer(self, other: "BankAccount", amount: int) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            self.history.append(("transfer_out", amount))
            self.history.append(("transfer_in", amount))
            return True
        
        return False




    



b=BankAccount()
print(b.get_balance())
print(b.deposit(100))
print(b.deposit(50))
print(b.withdraw(50))
print(b.get_balance())
print(b.get_history())

b.undo()
print(b.get_balance())
print(b.get_history())

b.undo()
print(b.get_balance())
print(b.get_history())
a1=BankAccount()
a2=BankAccount()    
a1.deposit(200)
print(a1.get_balance())
print(a2.get_balance())

a1.transfer(a2, 50)
print(a1.get_balance())
print(a2.get_balance())
print(a1.get_history())
print(a2.get_history())
