# 클래스 
print("\n  =========클래스==========\n")
result  = 0
#num 에서 받은 값을 이전에 계산한 결괏값에  더한 후 돌려주는 함수 
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
print(add(3))


print("\n  =========클래스==========\n")
#빼기 곱하기 등의 기능을 추가해야 한다면 함수 하나하나를 만들어야 한다.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))

print("\n========= cla2=======")

print(cal2.add(3))
print(cal2.add(7))

print("\n========= class=======")
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
b = FourCal()

a.setdata(4,2)
b.setdata(3,5)
print("a의 first :", a.first)
print("b의 first :", b.first)
print(a.second)


