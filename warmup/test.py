# counter10Krat = 0
# for x in range(0, 50):
#
#     print(x)
#     if x % 10 == 0:
#         print(x, "Yay its 10 kratnoe!")
#         counter10Krat += 1
#
# print("couter of total  ", counter10Krat)
#
# address = "Bat Yam , 9038 ZIP 38601, Israel"
# idex = "9038"
# if address.find(idex):  # bad check gets true even at -1
#     print("found! at positon ", address[address.find(idex):])
#     print("found right after sequence ", "\t", "<<", address[:address.find(idex)], ">>")
#
# testing = "TesTINg"
# print(testing.lower())
# print(testing.upper())
# print("pas" + "s" + "word")
# print("Ha" * 4)
#
# print(5.0 / 3)
# print(5 / 3)
# print(5 // 3)
# whole = 8 % 3
# remainder = 8 - whole
# print(8 % 3, remainder , whole)
#
# print("will do casting now")
#
#
# print(int ("1") +1 )
# stringfloatNumber = "3.345453"
# print(stringfloatNumber, "type ->", type(stringfloatNumber) , "type of casted- > ",  type(float(stringfloatNumber)))
#
# print (bool(""))
# print(bool(1))
# print(bool(None))
# print(None)
#
# a_word = "instead of camelCase"
# print(a_word)

item1 = [1, 2, 3, 4, 5, 6]
item2 = {1: [1, 2, 3, 4, 5]}
item3 = (1, 2, 3, 4, 5, 6)

print(type(item1))
print(type(item2))
print(type(item3))


class Account(object):
    def __init__(self, holder, account_number, balance, credit_line=0):
        self.Holder = holder
        self.Account_Number = account_number
        self.Balance = balance
        self.Creadit_Line = credit_line

    def transfer(self, target, amount):
        pass

    def deposit(self, amount):
        print("Balance before operation ", self.Balance)
        self.Balance += amount
        print("New balance is :", self.Balance)

    def withdraw(self, amount):
        if self.Balance < amount:
            print("Insufficient funds")
            return False
        else:
            print("remaning balance after withdrawal ", self.Balance - amount)
            self.Balance -= amount
            return True

    def balance(self):
        return self.Balance


ac03068633 = Account("Sergeim", "03068633", 100000000)

print(ac03068633.balance())
ac03068633.deposit(2000)
print(ac03068633.balance())
ac03068633.withdraw(3000)
print(ac03068633.balance())

my_list = [1.0, 'a', [1, 2, 3, 4, 5, 6, 7, 8], {1: 2}, True]

if int(my_list[0]) < my_list[-1]:
    print("Hey")
else:
    print(int(my_list[-1]))

print
my_list[1::2]  # stepping , we have a step  of 2
print
my_list[1:4]
