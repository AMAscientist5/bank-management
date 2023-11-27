
class Bank:
    users = []
    admin = 'Admin'
    bankBalance = 0
    totalLoan = 0
    loanActive = True
    withdrawActive=True

    def createUser(self, name, email, address, accountType):
        accNo=f'{name}{email}'
        userInfo = User(name, email, address, accountType, self,accNo)
        self.users.append(userInfo)
        return userInfo
    def loginUser(self,username):
        for user in self.users:
            if user.name==username:
              return user
        return None
    
    def depositBalance(self, amount):
        self.bankBalance += amount

    def checkBalance(self):
        print('\n---------welcome to bank------------')
        print(f'Total balance of the bank : {self.bankBalance} ')
        print('-------------------------------------')
        return ''

    def withdrawBalance(self, amount):
        self.bankBalance -= amount

    def updateTotalLoan(self, amount):
        self.totalLoan += amount

    def showTotalLoan(self):
        print('\n---------welcome to bank------------')
        print(f'Total loan amount of the bank : {self.totalLoan}')
        print('-------------------------------------')

    def showAllAcount(self):
      user_info = set()
      for user in self.users:
        user_info.add((user.name, user.accNo))

      print('\n--------all User Accounts------------')
      for name, acco in user_info:
        print(f'User: {name}, Account Number:{acco}')
      print('-------------------------------------')
      

    def deleteAccount(self, accNoIn):
        updated_users = [user for user in self.users if user.accNo != accNoIn]

        if updated_users != self.users:
            self.users = updated_users
            print('\n-------welcome to the bank-------')
            print(f'Account deleted successfully')
            print('-----------------------------------')
        else:
          print(f'{accNoIn} Account does not exist')

    
        

       
    def loanFeatureOnOff(self,value):
        if value ==1:
            self.loanActive=True
            print('\n-------welcome to the bank--------')    
            print(f'loan feature on successfully !!')
            print('-----------------------------------')
        elif value==0:
            self.loanActive=False
            print('\n------welcome to the bank---------')    
            print(f'loan feature off successfully !!')
            print('-----------------------------------')

    def withdrawFeatureOnOff(self,value):
        if value ==1:
            self.withdrawActive=True
            print('\n---------welcome to the bank----------')    
            print(f'Withdraw feature on successfully !!')
            print('------------------------------------')
        
        elif value==0:
            self.withdrawActive=False
            print('\n---------welcome our bank--------')    
            print(f'Withdraw feature off successfully !!')
            print('----------------------------------')
        


class User:
    transactionHistory = []
    loanLimit = 2
    balance = 0
    accNo=None

    def __init__(self, name, email, address, accountType, bank,accNo):
        self.name = name
        self.email = email
        self.address = address
        self.accountTupe = accountType
        self.bank = bank
        self.accNo=accNo
        self.bank.users.append(self)
        
        print('\n---------welcome to the bank------------')
        print(f'Account created successfully! account number: {self.accNo}')
        print('-------------------------------------')

    def deposit(self, amount):
        if amount < 0:
            print('\n---------welcome to the bank------------')
            print('invalid amount, deposit a positive amount')
            print('-------------------------------------')

        else:
            self.balance += amount
            self.bank.depositBalance(amount)
            description = 'deposit'
            info = {description: amount}
            self.transactionHistory.append(info)
            print('\n---------welcome to the bank------------')
            print(f'Deposit was successful! Current balance: {self.balance}')
            print('-------------------------------------')
    def moneyTransferAnotherAccount(self,accountNumber,amount):
        for  user in self.bank.users:
            if user.accNo==accountNumber:
                if amount<=self.balance:
                    user.balance+=amount
                    self.balance-=amount
                    self.bank.bankBalance+=amount
                    des='money transfer'
                    description = f'{des}- account number: {accountNumber} amount: {amount}'
                    info = {description: amount}
                    self.transactionHistory.append(info)
                    print('\n---------welcome to the bank------------')
                    print(f'Transfer account number : {accountNumber} amount: {amount} successfully !!')
                    print('--------------------------------------')
                    return
                else:
                    print('\n---------warning-------')
                    print('invalid amount')
                    print('--------------------------')
                    return
        print('---------warning--------')
        print('invalid account number')
        print('-----------------------')
        return



    def withdraw(self, amount):
        if self.bank.withdrawActive:
            if amount <= self.balance:
                self.balance -= amount
                self.bank.withdrawBalance(amount)
                description = 'withdraw'
                info = {description: amount}
                self.transactionHistory.append(info)
                print('\n---------welcome to the bank----------')
                print(f'Withdrawal was successful! Current balance: {self.balance}')
                print('-------------------------------------')

            else:
              print(f'\n----current balance: ({self.balance})----')
              print('invalid amount')
              print('-------------------------------------')
        else:
             print('\n---------welcome to the bank------------')
             print('----------the bank is bankrupt--------')
             print('-------------------------------------')
        

    def getBalance(self):
        print('\n------Account balance--------')
        print(f'Current balance: {self.balance}')
        print('---------------------------------')

    def getTransactionHistory(self):
        print('\n------ transaction history-----')
        for info in self.transactionHistory:
            for key, value in info.items():
                print(f'{key} --- {value}')
        print('------------------------------')

    def takeLoan(self, amount):
        if self.bank.loanActive:
            if self.loanLimit !=0 :
                self.balance += amount
                self.loanLimit -= 1
                self.bank.updateTotalLoan(amount)
                description = 'take loan'
                info = {description: amount}
                self.transactionHistory.append(info)
                print('\n------ welcome to the bank ---------')
                print(f'Loan was successful! loan limit: {self.loanLimit} times  balance: {self.balance}')
                print('\n-----------------------------------')
            else:
                print('\n------ welcome to the bank ------')
                print('Loan limit is finished')
                print('\n--------------------------------')
        else:
            print('\n--------- welcome to the bank -------')
            print('Loan feature is off. to get a loan can contact to admin')
            print('\n-------------------------------------')

    def transferTo(self):
        pass


sonali = Bank()

currentUser=None
flag=True
while(flag):
    if currentUser ==None:
            print("")
            print('To get banking facility get access Admin authority --')
            print('Use (Admin) key  word')
            authName=input('\n Write your access name: ')
            if sonali.admin==authName:
                currentUser=authName
            else:
                print('\n--------------warning-----------')
                print('\n invalid, please write (Admin)')
                print('--------------------------------')
    else:
        if currentUser !='Admin':
            print('chose option !!\n')
            print('1. Deposit')          
            print('2. Withdraw')          
            print('3. Check balance')          
            print('4. Take loan')          
            print('5. Check transaction history')          
            print('6. Money transfer to another user account')          
            print('7. User logout')          
            
            op=int(input('chose option: '))
            if op==1:
                amount=int(input('give deposit amount: '))
                currentUser.deposit(amount)
            elif op==2:
                amount=int(input('give withdraw amount: '))
                currentUser.withdraw(amount)
            elif op ==3:
                currentUser.getBalance()
            elif op==4:
                 amount=int(input('give loan amount: '))
                 currentUser.takeLoan(amount)
            elif op==5:
                currentUser.getTransactionHistory()
            elif op ==6:
                accountNumber=input('\n please write account number: ')
                amount=int(input('please write transaction amount: '))
                currentUser.moneyTransferAnotherAccount(accountNumber,amount)
            elif op==7:
                currentUser='Admin'
        else:
            print('--------------- ')
            print('chose option !!')
            print('---------------')
            print('0. User login')          
            print('1. Create an account  ')          
            print('2. Delete user account')          
            print('3. See all user accounts list')          
            print('4. Check total available balance of the bank')          
            print('5. Check the total loan amount')          
            print('6. Loan feature On/Off of the bank')          
            print('7. Withdraw feature On/Off of the bank')          
            print('8. Admin logout')          
            
            op=int(input('chose option: '))
            if op==0:
                info=input('\n account name: ')
                
                loggedUser=sonali.loginUser(info)
                if loggedUser:
                    currentUser=loggedUser
                else:
                    print('\n-----------warning-----------')
                    print('\ninvalid user')
                    print('--------------------------------')
                    
            elif op==1:
                name=input('write your name: ')
                email=input('write your email: ')
                address=input('write your address: ')
                acctupe=input('write your account type? (saving/current): ')
                sonali.createUser(name,email,address,acctupe)
            elif op==2:
                info=input('account number: ')
                sonali.deleteAccount(info)
            elif op ==3:
                sonali.showAllAcount()
               
            elif op==4:
                  sonali.checkBalance()
            elif op==5:
                sonali.showTotalLoan()
            elif op ==6:
                value=input('if you loan feature on/off please write (on/off) key word: ')
                if value=='on':
                    sonali.loanFeatureOnOff(1)

                elif value=='off':
                    sonali.loanFeatureOnOff(0)

                else:
                    print('\n--------------warning-----------')
                    print('invalid key word')
                    print('--------------------------------')

            elif op==7:
                value=input('if you withdraw feature on/off please write (on/off) key word: ')
                if value=='on':
                    sonali.withdrawFeatureOnOff(1)

                elif value=='off':
                    sonali.withdrawFeatureOnOff(0)

                else:
                    print('\n--------------warning-----------')
                    print('invalid key word')
                    print('--------------------------------')
            
            elif op==8:
                flag=False


            
