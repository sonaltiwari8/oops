class Account:
    balance = 0
    username = None

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"✅ withdrawal successfully, remaining balance {
                self.balance}")
        else:
            print("Insufficient balance ❌")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"✅ deposit successfully, total balance {
                self.balance}")
        else:
            print("Invalid deposit amount ❌")

    def check_balance(self):
        print(f"your available balance {self.balance}")


a1 = Account()
a2 = Account()
a3 = Account()

a1.deposit(2000)
a2.withdraw(2000)
a1.withdraw(500)

a1.check_balance() 


