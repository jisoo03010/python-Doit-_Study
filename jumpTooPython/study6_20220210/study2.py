#상속
class FurCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self): # 결과 값을 보여주는 메서드 
        result = self.first + self.second
        return result
    def mul(self): # 결과 값을 보여주는 메서드 
        result = self.first * self.second
        return result
    def sub(self): # 결과 값을 보여주는 메서드 
        result = self.first - self.second
        return result
    def div(self): # 결과 값을 보여주는 메서드 
        result = self.first / self.second
        return result


class MoreFourCal(FurCal):
    def pow(self):
        result = self.first ** self.second
        return result

print("\n")
# a = MoreFourCal(4,2)
# print(a.add())
# print(a.pow()) # 4의 2제곱 

# print("\n")
# a = FurCal(4, 0)
# print(a.div())


print("\n")

class SafeFourCal(FurCal):
     def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second



c = SafeFourCal(4, 0)
print(c.div())