# 볼 자료형 ?
"""
참과 거짓을 나타내는 자료형 
"""
from ntpath import join


a = [1, 2, 3, 4]
while a:
    print(a.pop())

# 연습 문제
print("\n======================연습 문제===================================\n")
# 1번.
korea = 80
english = 75
math = 55

print("문제 1번 국어 영어 수학의 평균 점수 ? :: ", (korea + english + math) / 3)


# 문제 2번 자연수 13이 홀수인지 짝수인지 판별 할수 있는 방뻡
print("\n========문제 2번 ===========\n")
if 13 % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

print("\n========문제 3번 ===========\n")
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print("연월일 : ", yyyymmdd)
print("숫자부분 : ", num)

print("\n========문제4번 ===========\n")
pin = "881120-1068234"
print(pin[7])

print("\n========문제5번 ===========\n")
a = "a:b:c:d"
print(a.replace(":", "#"))

print("\n========문제6번 ===========\n")
a = [1, 3, 5, 4, 2]
a.sort()
print(a)

a.reverse()
print(a)

print("\n========문제7번 ===========\n")
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

print("\n========문제8번 ===========\n")
a = (1, 2, 3)
a = a + (4,)
print(a)

print("\n========문제9번 ===========\n")

a = dict()
a[('a',)] = 'python'
print(a)

print("\n========문제10번 ===========\n")

a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

print("\n========문제11번 ===========\n")

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(aSet)
print(b)
