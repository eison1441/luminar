class Bank:
    accno:int

    balance:int

    ac_type:str

    coustomer_name:str

    def __init__(self,accno,balance,ac_type,coustomer_name):

        self.accno=accno

        self.balance=balance

        self.ac_type=ac_type

        self.coustomer_name=coustomer_name

    def deposit(self,amount):

        self.balance+=amount
        print(f"your aacount{self.accno} has been crediteed with amount{amount} available balance={self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print(f"insufficient balance in your account{self.accno}")
        else:
            self.balance-=amount
            print(f"your aacount{self.accno} has been debited with amount{amount} available balance={self.balance}")
    def get_balance(self):

        print("your available balance is ",self.balance)


Bank_instance1=Bank(1441,57000,"savings","Eison")
Bank_instance1.deposit(3000)
Bank_instance1.withdraw(5000)
Bank_instance1.get_balance() 
