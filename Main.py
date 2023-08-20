from Bank import Bank
from Person import User, Admin
import time


def main():
    bank = Bank('Sonali Bank')

    # create user
    user1 = User('Noyon Ahammed', 'noyon@gmail.com',
                 'Mollapara, Jashore', 1234)
    bank.create_account('user', 'student', user1)
    user2 = User('Sojon Ahammed', 'sojon@gmail.com',
                 'Mollapara, Jashore', 1235)
    bank.create_account('user', 'student', user2)
    user1.deposit(1000, bank)
    user1.withdraw(200, bank)
    user1.transfer_money(300, user2)
    user1.take_loan(bank)

    # create admin
    admin = Admin('Admin Khan', 'admin@gmail.com', 'RN Road', 1236)
    bank.create_account('admin', 'manager', admin)
    user1.take_loan(bank)
    user1.take_loan(bank)
    user2.take_loan(bank)
    admin.change_loan_status('off', bank)
    user2.take_loan(bank)
    admin.check_balance_of_bank(bank)
    admin.check_loan_balance_of_bank(bank)


if __name__ == "__main__":
    main()
