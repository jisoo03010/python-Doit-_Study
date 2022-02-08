# 키워드 파라미터 

def print_kwargs(**kwargs):
    print(kwargs)

#  ** = 딕셔너리로 만들어져서 출력된다.
print_kwargs(a=1)

def add_and_mul(a, b):
    return a+b, a*b

#리턴값을 하나 이상 출력시키려고하면 이와 같이 튜플을 반환하게 된다.
#이유 ? 함수의 결괏값은 언제나 하나이기 때문이다.
result1, result2  = add_and_mul(3,4)
result  = add_and_mul(3,4)
print(result) # 튜플반환 
print(result1, result2) #3+4, 3*4 각각의 값을 반환 


def add_and_mul(a,b):
    return a+b
    return a*b #실행되지 않음

a = add_and_mul(2,3)
print(a)

#return 의 또다른 쓰임새 
def say_nick(nick):
    if nick =="바보":
        return #함수를 빠져나감 
    print("나의 별명은 %s입니다." %nick)


print(say_nick("바보"))
print(say_nick("김치수\n"))

print("\n===========매개변수에 초깃값 미리 설정하기============")
#매개변수에 초깃값 미리 설정하기
def say_myself(name, old , man=True):
    print("나의 이름은  %s입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")


profile  = say_myself("김지수", 19, False)
print(profile)

print("\n====함수 밖에서 변수 사용해 보기=====")


a =1
def vartest(a):
    a= a+1
    return a
a = vartest(a)
print(a)


print("\n========global 명령어 사용하기 ========")
#추천하지 않음 
# 이유 ? 함수는 독립적으로 존재하는 것이 좋기 때문이다.

a = 3
def num():
    global a
    a = a +1

num()
print(a)

print("\n========lambda(람다 사용해보기)=======")
add = lambda a,b : a+b
result = add(3,4)
print(result)

print("def로 표기하면 다음과 같음")
#def로 표기하면 다음과 같음
def add(a, b):
    return a+ b

result  = add(3, 4)
print(result)