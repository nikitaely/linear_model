from main import *

green_bank = Bank()
red_bank = Bank()

Client.default_info()

student = Client(green_bank)
teacher = Client(red_bank)

student.info()
print(teacher)

a = SmallHouse(10000)

student.buy_house(a, 1000)

student.earn_money(10000)

student.buy_house(a, 1000)

print(student)