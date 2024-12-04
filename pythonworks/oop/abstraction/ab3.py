class Bankaccount:
    def __init__(self,coustomer_name,mpin,account_type,balance):
        self.coustomer_name=coustomer_name
        self.__mpin=mpin
        self.account_type=account_type
        self.__balance=balance

    def get_balance(self):
        print(self.__balance)


    def account_tpye_chk(self):
        print(self.account_type)


    def __str__(self):
        return self.coustomer_name
    
bank_account_instance=Bankaccount("Eison",4002,"savings",2700)

bank_account_instance.get_balance()
print(bank_account_instance)
bank_account_instance.account_tpye_chk()
print(bank_account_instance.get_balance)