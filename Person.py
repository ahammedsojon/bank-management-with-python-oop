from datetime import datetime, date
from Bank import Bank


class Person:
    def __init__(self, name, email, address, nid) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.nid = nid


class User(Person):
    def __init__(self, name, email, address, nid) -> None:
        self.__id = None
        self.__account_number = None
        self.occupasion = None
        self.transaction = {}
        self.got_loan = 0
        super().__init__(name, email, address, nid)

    def set_info(self, id, role):
        self.__id = f'{self.name}-{id+1}'
        self.__account_number = 1000 + id + 1
        self.occupasion = role
        self.__balance = 0

    @property
    def check_balance(self):
        return f'Your currnet balance is {self.__balance}'

    def deposit(self, amount, bank):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        else:
            if amount > 0:
                self.__balance += amount
                bank.add_balance(amount)
                now = datetime.now()
                current_date = date.today().strftime("%b-%d-%Y")
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                str = f'You have deposited {amount}tk on {dt_string}'
                if current_date not in self.transaction:
                    self.transaction[current_date] = [str]
                else:
                    self.transaction[current_date].append(
                        str)
                print(
                    f'You have successfully deposited {amount}tk. Your current balance is {self.__balance}tk.')
            else:
                print(f'You have not sufficient balance to deposit.')

    def withdraw(self, amount, bank):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        else:
            if amount < self.__balance:
                self.__balance -= amount
                bank.reduce_balance(amount)
                now = datetime.now()
                current_date = date.today().strftime("%b-%d-%Y")
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                str = f'You have withdraw {amount}tk on {dt_string}'
                if current_date not in self.transaction:
                    self.transaction[current_date] = [str]
                else:
                    self.transaction[current_date].append(
                        str)
                print(
                    f'You have successfully withdraw {amount}tk. Your current balance is {self.__balance}tk.')
            else:
                print(
                    f'You have not enough balance to withdraw. Your current balance is {self.__balance}')

    def transfer_money(self, amount, other_account):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        elif amount > self.__balance:
            print(f'You have not sufficient balance to transfer.')
        elif amount <= 0:
            print('Please enter valid amount')
        else:
            if other_account.__account_number != None:
                self.__balance -= amount
                other_account.__balance += amount
                now = datetime.now()
                current_date = date.today().strftime("%b-%d-%Y")
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                str = f'You have transfered {amount}tk on {dt_string}'
                if current_date not in self.transaction:
                    self.transaction[current_date] = [str]
                else:
                    self.transaction[current_date].append(
                        str)
                if current_date not in other_account.transaction:
                    other_account.transaction[current_date] = [
                        f'You have got {amount}tk from {self.name} on {dt_string}']
                else:
                    other_account.transaction[current_date].append(
                        f'You have got {amount}tk from {self.name} on {dt_string}')
                print(
                    f'You have successfully transfered {amount}tk to {other_account.name}. Your current balance is {self.__balance}tk.')
            else:
                print(f'Please enter a valid account to transfer money.')

    def transaction_history(self):
        for value in self.transaction.values():
            for each in value:
                print(each)

    def take_loan(self, bank):
        if bank.check_loan_status() == False:
            print('Currently loan feature is off by the system.')
        elif self.got_loan == 2:
            print('You have already taken maximum times of loan.')
        else:
            self.got_loan += 1
            bank.add_loan_balance(self.__balance)
            self.__balance += self.__balance
            print(
                f'You have successfully got loan. Your current balance is {self.__balance}tk,')

    def __repr__(self) -> str:
        print(self.__account_number, self.__id)
        return ''


class Admin(Person):
    def __init__(self, name, email, address, nid) -> None:
        self.__id = None
        self.department = None
        super().__init__(name, email, address, nid)

    def set_info(self, id, role):
        self.__id = f'{self.name}-{id+1}'
        self.department = role

    def check_balance_of_bank(self, bank):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        else:
            return bank.check_balance

    def check_loan_balance_of_bank(self, bank):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        else:
            return bank.check_loan_balance

    def change_loan_status(self, status, bank):
        if self.__id == None:
            print(f'{self.name}, please create an account first!')
        else:
            bank.loan_status(status)

    def __repr__(self) -> str:
        print(f'{self.name}, {self.department}')
        return ''
