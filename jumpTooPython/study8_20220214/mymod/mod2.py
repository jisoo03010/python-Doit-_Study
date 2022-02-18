#클래스나 변수 들을 포함한 모듈
#mod2.py

PI = 3.141592

#원의 넓이를 구하는 math클래스
class Math:
    def solv(self, r):
        return PI * (r ** 2)


#두 값을 더하는 add함수 
def add(a, b):
    return a+ b