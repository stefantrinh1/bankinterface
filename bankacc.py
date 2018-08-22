# a bank account
import random

class Bank():
    account_list = []
    account_types = ["standard","premier"]

    def create(self):
        print("Thank you for Choosing to create an Account with us.")
        acc_type =""
        while acc_type not in self.account_types:
            print("These are the accounts available to open",self.account_types)
            acc_type = input("which would you like to open? : ")

        acc_type.lower()
        accrand = self.generated_account_no()
            
        if acc_type == "standard":
            s001 = Standard(accrand, self.account_list)
            self.account_list.append(s001)
            print("please notedown your account number")
            print("you account number is:", accrand)
        else:
            p001 = Premier(accrand, self.account_list)
            self.account_list.append(p001)
            print("please notedown your account number")
            print("you account number is:", accrand)

    def generated_account_no(self):
        accountno = ""
        generatednumbers = [str(num) for num in range(6)]
        random.shuffle(generatednumbers)
        for num in generatednumbers:
            accountno += num
        for a in self.account_list:
            while accountno == a.accno:
                accountno = ""
                generatednumbers = [str(num) for num in range(6)]
                random.shuffle(generatednumbers)
                for num in generatednumbers:
                    accountno += num
        return accountno

    def services(self):
        choice = ""
        while choice != "0":
            print("""
            welcome to The Bank

            0 - Leave Bank
            1 - Create Account
            2 - Cash Services
            """
            )
            success = None
            choice = input("please enter the action you would like to take: ")
            if choice == "1":
                self.create()
            elif choice == "2":
                login = input("please enter your account number :  ")
                for x in self.account_list:
                    if login == x.accno:
                        print("account found")
                        success = True
                        transaction = CashMachine(x)
                        transaction.main()
                if success != True:
                    print("Account not found")
            elif choice =="0":
                pass
            else:
                print("action not found. Please try again.")

class Standard():
    def __init__(self, accno, account_list, funds = 0):
        print("bank account created")
        self.funds = funds
        self.accno = accno
        self.account_list = account_list
    
    def deposit(self):
        deposit = int(input("how much would you like to deposit? : "))
        print("you are about to deposit: £",deposit)
        confirm = input("Please confirm Y? : ")
        confirm.lower()
        if confirm == "y":
            self.funds +=deposit
            print("you have sucessfully deposited : £",deposit)
            print("your balance now stands at: £",self.funds)
        else: 
            print("transaction cancelled")
        
    
    def withdraw(self):
        withdraw = int(input("how much would you like to withdraw? : "))
        if withdraw > self.funds:
            print("insufficient funds")
        print("you are about to withdraw = £",withdraw)
        confirm = input("Please confirm Y? : ")
        confirm.lower()
        if confirm == "y":
            self.funds -=withdraw
            print("you have withdrawn = £",withdraw)
        else: 
            print("transaction cancelled")
    
    def check(self):
        print("your Balance is: £",self.funds)
    
     
    def transfered(self, transamount):
        self.funds +=transamount
        print("you have transfered: £",transamount)

        
    
    def transfer(self):
        transaccno = input("please enter the account number you would like to transfer the money too : ")
        transamount = int(input("please enter how much you would like to transfer : "))
        success = None
        if transamount <= self.funds:
            for x in self.account_list:
                if transaccno == x.accno:
                    success = True
                    self.funds -= transamount
                    print("account found")
                    x.transfered(transamount)

            if success != True:
                print("Account Not Found")
        else:
            print("you have insufficient funds to transfer")
    
    def checkinterest(self):
        print("No Interest is earned on this account")

                 


class Premier(Standard):
    
    def __init__(self, accno, account_list, funds = 0, interest = 2):
        self.account_list = account_list
        self.interest = interest
        self.funds = funds
        self.accno = accno

    def checkinterest(self):
        print("interest earning on this account is:", self.interest,"%")

class CashMachine():
    def __init__(self,account):
        self.account = account

    def main(self):

        choice = ""
        while choice != "0":
            print("""
            welcome to your account

            0 - log off
            1 - Deposit Money
            2 - Withdraw Money
            3 - Check Balance
            4 - Transfer Money
            5 - check interest rate
            """ )
            choice = input("please enter the action you would like to take : ")

            if choice == "1":
                self.account.deposit()
            
            elif choice == "2":
                self.account.withdraw()
            
            elif choice == "3":
                self.account.check()
            
            elif choice == "4":
                self.account.transfer()
            elif choice == "5":
                self.account.checkinterest()
            
def main():
    bank = Bank()
    print("welcome to The Bank")
    bank.services()

main()
print("Thank you, Goodbye")






