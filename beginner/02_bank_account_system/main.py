import datetime

def transaction_time(func):
        def wrapper(*args):
            print(f"You {func.__name__}ed at {datetime.datetime.now()}")
            return func(*args)
        return wrapper
    
class BankAccount:
    balance: int = 0
    def __init__(self, acc_num: int, acc_holder: str, balance: int):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.__balance = balance
        self.transaction = 0

        
    @property   
    def get_bal(self):
        return self.__balance
    
    @get_bal.setter
    def set_bal(self, new_bal):
        if isinstance(self.__balance, int):
            self.__balance = new_bal
            return self.__balance

    @transaction_time 
    def deposit(self, amount: int):
        if isinstance(amount, int):
            if amount > 0:
                self.__balance += amount 
                self.transaction += 1
                return self.__balance
            else:
                return "Please enter non-negetive number"
        else:
            print("Please enter a valid amount")
    
    @transaction_time
    def credit(self, amount: int):
        if isinstance(amount, int):
            if amount <= self.__balance and amount > 0:
                self.__balance -= amount
                self.transaction += 1
                return amount
            else:
                return "Please enter a non-negetive number"
        else:
            return "Please enter a valid amount"

    def check_balance(self):
        return f"User {self.acc_holder} balance is {self.__balance}"
    
    @property
    def trans_histry(self):
        return f"Transaction history: {self.transaction}" 
    
    
class SavingAccount(BankAccount):
    def __init__(self):
        super().__init__(123, "Wajid", 20000)
        
    def add_interest(self, rate: int):
        rate += self.__balance
        return rate
    
    def check_balance(self):
        return f"User {self.acc_holder.capitalize} balance is {self.balance}",
    
bank = BankAccount(129082973562, "Marjan", 100)
print(bank.deposit(100)) 
print(bank.check_balance()) # 200
print(bank.credit(90))
print(bank.check_balance()) # 100
print(bank.trans_histry)