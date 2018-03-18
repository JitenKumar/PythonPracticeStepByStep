class Book():
    def __init__(self,name,author,pages,publisher):
        self.name = name
        self.author = author
        self.pages = pages
        self.publisher = publisher

    def __len__(self):
        return self.pages

    def __del__(self):
        return f"A book object has been deleted"

    def __str__(self):
        return f"book {self.name} by {self.author}"


my_book = Book('PythonTheHeardWay','Jiten',200,'MCH')
length = len(my_book)
print(length)

## practice


class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, money):

        self.balance = self.balance + money
        print('Deposit accepted')

    def withdraw(self, money):
        if self.balance >= money:
            self.balance = self.balance - money
        else:
            print('Funds Unavailable')

    def __str__(self):
        return f"Account Owner: {self.owner} \nAccount balance: ${self.balance}"

    # 1. Instantiate the class

    acct1 = Account('Jose', 100)