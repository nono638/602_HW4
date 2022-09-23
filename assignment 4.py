#Made Noah Collin and Melissa Bowman on 9/22/2022
"""Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
● A method called deposit() that allows the user to make deposits into their balance.
● A method called withdrawal() that allows the user to withdraw from their balance.
● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
in your withdrawal() method.
● Use the __str__() method in order to display the bank name, owner name, and current
balance.
● Make a series of deposits and withdrawals to test your class.

"""
print("Q1:")


class BankAccount:

    def __init__(self, bankname, firstname, lastname, balance=0.0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def __str__(self):
        return ("{} {} {} ${}".format(self.bankname, self.firstname,
                                      self.lastname, self.balance))


if (__name__ == "__main__"):

    def testQ1():
        testAccount = BankAccount("Chase", "Noah", "Collin", 555)
        #(self, bankname, firstname, lastname,
        #balance = 0.0):

        testAccount.withdrawal(554)
        print(testAccount.balance)
        testAccount.deposit(44)

        print(testAccount.balance)

        #print(dir(BankAccount))

        #print(str(BankAccount))

        #print(testAccount.__str__())

        print(str(testAccount))

        import random
        random.seed(42)
        for i in range(10):
            randomNum = random.choice(range(1, 100))
            testAccount.deposit(randomNum)
            print("  Depositing ${}...".format(randomNum))
            print("New Balance ${}".format(testAccount.balance))

    testQ1()
print()
print("Q2")
"""Q2: Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create...
● A method called render() that prints out to the screen a box made with asterisks of
length and width dimensions
● A method called invert() that switches length and width with each other
● Methods get_area() and get_perimeter() that return appropriate geometric calculations
● A method called double() that doubles the size of the box. Hint: Pay attention to return
value here.
● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
their respective lengths and widths are identical.
● A method print_dim() that prints to screen the length and width details of the box
● A method get_dim() that returns a tuple containing the length and width of the box
● A method combine() that takes another box as an argument and increases the length
and width by the dimensions of the box passed in
● A method get_hypot() that finds the length of the diagonal that cuts through the middle
● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
box2 and box3 respectively
● Print dimension info for each using print_dim()
● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
screen accordingly
● Combine box3 into box1 (i.e. box1.combine())
● Double the size of box2
● Combine box2 into box1"""


class Box:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        for i in range((self.length)):
            for j in range((self.width)):
                if (i == 0 or i == (self.length) - 1 or j == 0
                        or j == (self.width) - 1):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def double(self):
        self.width, self.length = self.width * 2, self.length * 2

    def __eq__(self, box2):
        #Two boxes are equal if
        #their respective lengths and widths are identical
        if ((self.length == box2.length) and (self.width == box2.width)):
            return True
        else:
            return False

    def print_dim(self):  # represenation
        print("length: {}\nwidth:  {}".format(self.length, self.width))

    #get_dim() that returns a tuple containing the length and width of the box
    def get_dim(self):
        return (self.length, self.width)  #parens for tuple

    def get_hypot(self):
        #a^2 + b^2 = c=2
        return self.length**2 + self.width**2

    #combine() that takes another box as an argument and increases the length
    def combine(self, otherBox):
        self.length += otherBox.length
        self.width += otherBox.width


#-------------------------------------
# Testing:
if (__name__ == "__main__"):

    def testQ2():
        #inital box
        test_box = Box(4, 9)
        test_box.print_dim()
        test_box.render()

        #invert the box
        print("inverting...")
        test_box.invert()
        test_box.print_dim()
        test_box.render()

        #double the box
        print("doubling...")
        test_box.double()
        test_box.print_dim()
        test_box.render()

        #test_box2 = Box(9*2, 4*2) # test_box inverted earlier
        #test_box3 = Box(5,6)
        #print(test_box2) #uses __repr__ function
        #print("test_box2 == test_box : {}".format(test_box2 == test_box) )
        #print("test_box3 == test_box: {}".format(test_box3 == test_box) )
        #print_dim(test_box3)

        #Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
        #box2 and box3 respectively
        #● Print dimension info for each using print_dim()
        box1, box2, box3 = Box(5, 10), Box(3, 4), Box(5, 10)
        boxes = [box1, box2, box3]
        for i in range(len(boxes)):
            print("box" + str(i + 1) + ":")
            boxes[i].print_dim()
        print()

        print("box1 == box2 : {}".format(box1 == box2))
        print("box1 == box3 : {}".format(box1 == box3))
        #Combine box3 into box1 (i.e. box1.combine())
        print("Combining box 1 and 3....")
        print("Box1 before combining: ")
        box1.print_dim()
        print("Box3 before combining: ")
        box3.print_dim()
        box1.combine(box3)
        print("box1 after combined with box3:")
        box1.print_dim()
        print()

        #● Double the size of box2
        print("Doubling box 2")
        print("Box2 before doubling: ")
        box2.print_dim()
        box2.double()
        print("box2 after doubling:")
        box2.print_dim()

        print()

        #● Combine box2 into box1"""
        print("Combining box 1 and 2....")
        print("Box1 before combining: ")
        box1.print_dim()
        print("Box2 before combining: ")
        box2.print_dim()
        box1.combine(box2)
        print("box1 after combined with box2:")
        box1.print_dim()
        print()

    testQ2()
