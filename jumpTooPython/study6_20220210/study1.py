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


# a = FurCal()
# b= FurCal()
# print("\n ========setdata A===========\n")
# a.setdata(3,4)
# print("더하기 : ",a.add())

# print("\n ========setdata B===========\n")
# b.setdata(6,5)

# print("더하기 : ",b.add())
# print("곱하기 : ",b.mul())
# print("빼기 : ",b.sub())
# print("나누기 : ",b.div())

# print("\n======== __init__ ==========\n")



c = FurCal(4,2)   
print(c.first)
print(c.second)    
print("c.add() : ", c.add())