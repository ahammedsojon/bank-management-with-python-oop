class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__balance = 0
        self.admins = []
        self.users = []
        self.__loan_available = True
        self.__loan_balance = 0

    @property
    def check_balance(self):
        print(f'Current total balance is {self.__balance}tk.')

    @property
    def check_loan_balance(self):
        print(f'Current total loan balance is {self.__loan_balance}tk.')

    def create_account(self, type, role, person):
        if type == 'user':
            person.set_info(len(self.users), role)
            self.users.append(person)
        else:
            person.set_info(len(self.admins), role)
            self.admins.append(person)

    def add_balance(self, amount):
        self.__balance += amount

    def add_loan_balance(self, amount):
        self.__loan_balance += amount

    def reduce_balance(self, amount):
        self.__balance -= amount

    def loan_status(self, status):
        if status == 'off':
            self.__loan_available = False
        else:
            self.__loan_available = True

    def check_loan_status(self):
        return self.__loan_available
