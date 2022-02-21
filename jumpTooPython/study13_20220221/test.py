from audioop import add
from traceback import print_tb


class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator) :
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

print("\n\n Q2======")
class Calculator:
    def __init__(self):
        self.value = 0

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = "100보다 커서 값을 나타낼 수 없음"
cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(99)
print(cal2.value)

print("\n\n Q3======")
print(chr(ord('a')) == 'a')

print("\n\n Q4======")

def positive(x):
    return x > 0
print(list(filter(positive, [1, -2, 3, -5, 8, -3])))



print(list(filter(lambda x:  x > 0, [1, -2, 3, -5, 8, -3])))
 
print("\n\n Q5======")
print(int('0xea', 16))

print("\n\n Q6======")
def add(x):
    return x * 3
print(list(map(add, [1,2,3,4])))
print(list(map(lambda x: x * 3, [1,2,3,4])))

print("\n\n Q7======")
a = [-8, 2 , 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))

print("\n\n Q8======")
print(round(17 / 3, 4))

print("\n\n Q9======")
import sys
numbers = sys.argv[1:]
result = 0
for  number in numbers:
    result += int(number)
print(result)


print("\n\n Q10======")
import time
print(time.strftime('%x %X', time.localtime(time.time())))


print("\n\n Q11======")
import random
for i in range(6):
   print(random.randint(1, 45)) 
