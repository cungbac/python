from abc import ABCMeta, abstractmethod

class Account:
    @abstractmethod
    def createAccount(self, email, password):
        pass

    @abstractmethod
    def authenticate(self, email, password):
        pass

    @abstractmethod
    def withdraw(self, withdrawAmount):
        pass

    @abstractmethod
    def deposit(self, depositAmount):
        pass

    @abstractmethod
    def displayBalance(self):
        pass

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount = {}
    
    def createAccount(self, email, name, password, deposit = 0):
        if email not in self.savingsAccount.keys():
            self.accountEmail = email
            self.savingsAccount[email] = [name, hash(password), deposit]
            print('Your account has been created')
        else:
            print('This email address already exists')
    
    def authenticate(self, email, password):
        if email in self.savingsAccount.keys():
            if hash(password) == self.savingsAccount[email][1]:
                print('Login successfully')
                self.accountEmail = email
                return True
            else:
                print('Wrong password')
                return False
        else:
            print('Email has not registered')
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccount[self.accountEmail][2]:
            print('Insufficient balance')
        else:
            self.savingsAccount[self.accountEmail][2] -= withdrawAmount
            print('Withdrawal was successful')
            self.displayBalance()
    
    def deposit(self, depositAmount):
        self.savingsAccount[self.accountEmail][2] += depositAmount
        print('Deposit was successful')
        self.displayBalance()

    def displayBalance(self):
        print('Available balance: ',self.savingsAccount[self.accountEmail][2])


# User interface
savingsAccount = SavingsAccount()

while True:
    print('Enter 1 to create a new account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to exit')

    # Create a new account
    userChoice = int(input())
    
    if userChoice == 1:
        print('Enter your email')
        email = input()
        print('Enter your name')
        name = input()
        print('Enter your password')
        password = input()
        
        while True:
            print('Confirm your password')
            pass_confirm = input()

            if password != pass_confirm:
                print('Wrong password confirm')
                print('Please try again')
            else:
                print('Enter your deposit')
                deposit = int(input())
                savingsAccount.createAccount(email, name, password, deposit)
                break
            
    # Login to an existing account
    elif userChoice == 2:
        print('Enter your email')
        email = input()
        print('Enter your password')
        password = input()
        ath_status = savingsAccount.authenticate(email, password)
        if ath_status == True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display available balance')
                print('Enter to go back to the previous menu')

                userChoice = int(input())
                if userChoice == 1:
                    print('Enter your withdraw amount')
                    withdrawAmount = int(input())
                    print(withdrawAmount)
                    savingsAccount.withdraw(withdrawAmount)
                elif userChoice == 2:
                    print('Enter your deposit amount')
                    depositAmount = int(input())
                    print(depositAmount)
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccount.displayBalance()
                elif userChoice == 4:
                    break
    # Exit
    elif userChoice == 3:
        print('Thank you for your transaction')
        quit()
    else:
        print('Please press 1 or 2 or 3')