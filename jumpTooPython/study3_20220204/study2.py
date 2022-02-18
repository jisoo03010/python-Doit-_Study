# 함수
def add(a, b):  # 매개 변수
    return a + b


a = 3
b = 2
c = add(a, b)  # 인수
print("\n", c)

print("\n===========입력값이 없는 함수============\n")


def say():
    return "hi"


print(say())

print("\n===========결과 값이 없는 함수============\n")


def add(a, b):
    print("%d , %d 의 합은 %d입니다." % (a, b, a+b))


add(3, 4)

# 매개변수 지정해서 호출하기
print("\n===========매개변수 지정해서 호출하기============\n")


def add(a, b):
    return a + b


result = add(a=3, b=4)
print(result)


print("\n===========여러개의 입력값을 받는 함수 만들기 ============\n")


def add_maney(*args):
    result = 0
    for i in args:
        result = result + i
    return result


result = add_maney(1, 2, 3)
print(result)
result = add_maney(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

print("\n===========여러개의 입력값을 받는 함수  예제 1 ============\n")


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
