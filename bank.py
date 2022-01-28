class BankingApp:
    """Bank class"""
    print('Welcome to your Banking App')


    def __init__(self):
        self.balance = 0.00

    def deposit(self):
        amount = float(input('Input amount to deposit:    '))
        self.balance += amount
        with open('deposit.txt', 'a') as file:
            file.write(f'\nYou deposited:\t {amount}\t\t\t\t Balance:{self.balance}')
            account.display()

    def withdrawl(self):
        amount = float(input('Input amount you want to withdrawl:   '))
        if self.balance >= amount:
            self.balance -= amount
            with open('withdrawl.txt', 'a') as file:
                file.write(f'\nYou withdrew:\t {amount}\t\t\t\t Balance:{self.balance}')
                account.display()
        else:
            print('insuffient balanace')

    def display(self):
        print(f'Balance is:\t\t {self.balance}')

account = BankingApp()

while True:
    user = input('Do you want to Deposit or Withdrawl.. command: d or w and q to exit:    ')
    if user == 'd':
        account.deposit()
    elif user == 'w':
        account.withdrawl()
    elif user == 'q':
        exit()
