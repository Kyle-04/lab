class Account:
    def __init__(self, name: str):
        self.__account_name: float = 0
        self.__account_balance: float = 0
        '''
        This will create the Account class and set the default account balances to 0.
        '''

    def deposit(self, amount: float):
        self.amount: float = float(input('Enter deposit amount: '))
        if self.amount <= 0:
            return False
        else:
            self.__account_balance += self.amount
            return True
    '''
    The deposit function will take a float amount as input and add it to the account balance if the value entered
    is greater than zero.
    '''
    def withdraw(self, amount: float):
        self.amount: float = float(input('Enter withdraw amount: '))
        if self.amount <= 0:
            return False
        else:
            self.__account_balance -= self.amount
            return True
    '''
    The withdraw function will take a float amount as input and subtract it from the account balance if the
    value entered is greater than zero.
    '''

    def get_balance(self):
        return self.__account_balance
    '''
    This function just returns the account balance to be tested.
    '''

    def get_name(self):
        return self.__account_name
    '''
    This function just returns the account name to be tested.
    '''
