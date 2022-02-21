#내장 함수 
from typing import Type
from unittest import result


print("\nabs함수 ===")
#숫자의 절댓값을 돌려주는 함수 
print("=> abs(3), abs(-19) : ", abs(3), "," ,abs(-19))

print("\nall함수 ===")
# all()은 반복가능한 자료형 x를 입력인수로 받으며 이x가 모두 참이면 true, 거짓이 하나라도 있으면  False를 돌려준다.
print("=>", all([1,2,3,33,45,2,21]))
print("=>", all([1,2,3,0,45,2,21])) # 0이 포함되어 있으므로 False 출력


print("\nany함수 ===")
#하나라도 참이면 True , x가 모두 거짓일 때만 False를 돌려줌
print("=>", any([1,0,0,0,0,0,0,0]))
print("=>", any([0,0,0,0,0,0,0,0]))
print("=>", any([0,""])) #리스트 자료형에서 0과 "" 빈 문자열은 모두 거짓이므로  False 반환


print("\nchr함수 ===")
#아스키 코드 값을 입력받아 코드에 해당하는 문자를 출력하는 함수 
print("chr(93) => ", chr(93))
print("chr(93) => ", chr(99))

print("\ndir함수 ===")
#객체가 자체적으로 가지고 있는 변수나 함수를 보여준다
print("\n\n\n ========= 리스트 관련 함수==========\n ")
print("리스트 관련 함수 => ", dir([1,2,3]))
print("\n\n\n ========= 딕셔너리 관련 함수 ==========\n")
print("딕셔너리 관련 함수 => ",dir((1,2,3,4)))


print("\n\n\ndivmod함수 ===")
# 두 개의 숫자를 입력 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수 
print("(몫, 나머지) => ", divmod(3,2)) # 결과 (몫, 나머지)


print("\nenumerate함수 ===")
## enumerate = "열거하다"
# 순서가 있는 자료형을 입력받아 인덱스 값을 포함한 enumerate 객체를 돌려준다.
# for 문과 함께 자주 사용된다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i , name)

print("\neval함수 ===")
# 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
a = eval('1+2')
print(a)
b = eval('divmod(4,3)')
print(b)


print("\nhex함수 ===")
#정수 값을 입력 받아 16진수로 변환하여 돌려주는 함수이다.
a= hex(30)
print(a)

print("\nid함수 ===")
# 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수이다.
#모두 같은 객체를 가리킴
a = 3
print("id(3) => ", id(3))
print("id(a) => ",id(a))
b = a
print("id(b) => ",id(b))


print("\ninput함수 ===")
#사용자의 입력을 받는 함수 
# a = input()
# print(a)
# b = input("Enter: ")


print("\nint함수 ===")
print(int('3'))
print(int(9.532))

#2진수로 표현된 11의 10진수 값은 다음과 같이 구한다
print(int('11', 2))
#16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
print(int('1A', 16))

print(hex(26)) 


print("\nisinstance함수 ===")
#isinstance(object, class) : 1번 인수 = 인스턴스, 2번 인수 = 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 반환한다.
class Person: pass #아무 기능없는 Person 클래스 생성
a = Person() # Person클래스의 인스턴스 a생성
print(isinstance(a , Person))

b = 3
print(isinstance(b , Person)) # false  : b는 person클래스의 인스턴스가 아닌 일반 정수 변수이다.


print("\nlen함수 ===")
#len(s)은 입력값 s의길이를 돌려주는 함수이다.
print('hello의 길이 : ',len('hello'))
print('array의 길이 : ',len([1,2,3,4,56,7,8,8]))
print('tuple의 길이 : ', len((1, 'a')))

print("\nlist함수 ===")
#반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수 
print(list('python'))
print(list((1,2,3))) # 튜플을 리스트로 변경

print("\nmap함수 ===")
#입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

print("\nMap함수를 사용하여 더 간단하게 함 ======")
def two_times(x):
    return x*2
a = list(map(two_times, [1,2,3,4]))
print(a)

print("\nlambda를 사용하여 더 간단하게 함 ======")
print(list(map(lambda a : a*2, [1,2,3,4])))


print("\nmax함수 ===")
a = max([1,2,3,4,53,2,24])
b = max('python')
print(a)
print(b)


print("\nmin함수 ===")
a = min([1,2,3,4,53,2,24])
b = min('python')
print(a)
print(b)


print("\noct함수 ===")
#정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
a = oct(34)
print(a)


print("\nopen함수 ===")
#파일 객체를 돌려주는 ㅎ마수 이다.
# f = open("binary_file", "rb") #바이너리 읽기 모드 

# #fread, fread2는 같은 읽기 모드 이다.
# fread = open("read_mode.txt", "r")
# fread2 = open("read_mode.txt")
# #추가 모드
# fappend = open("append_mode.text", "a")


print("\nord함수 ===")
#문자의 아스키 코드 값을 돌려주는 함수
#chr과 반대 되는 함수이다.
print(ord('a'))
print(ord('0'))

print("\npow함수 ===")
#pow(x, y) x와 y를 제곱한 결괏값을 돌려주는 함수이다.\
print(pow(3, 4)) # 3의 4의 제곱
print(pow(2, 2)) # 2의 제곱

print("\nrange함수 ===")
#fro 문과 함께 자주 쓰임
print(list(range(5))) # range함수는 0부터 시작한다.
#range의 인수가 2개일 경우
print(list(range(2, 8))) # 2  ~ 8전까지 list로 출력 #########끝 숫자는 포함하지 않는다.
#range의 인수가 3개일 경우
print(list(range(1, 10 , 2))) # 1부터 9까지, 숫자사이의 거리는 2


print("\nround함수 ===")
# 숫자를 입력받아 반올림 해주는 함수 
print(round(3.5))
print(round(3.495, 2)) # 소수접 2자리 까지만 반올림하여 표시

print("\nsorted함수 ===")
# 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3, 4,2,1]))
print(sorted(['a', 'c', 'd', 'b']))
print(sorted("zero"))
print(sorted((1,4,2)))


print("\nstr함수 ===")
#문자열 혀태로 객체를 변환하여 돌려주는 함수이다.
print(str(3))
print(str('hi'))
print(str('hi'.upper())) # upper () => 대문자로 변경

print(type(str(3)))

print("\nsum함수 ===")
a= sum([1, 2, 3])
a= sum((2, 3, 4))
print(a)

print("\ntuple함수 ===")
print(tuple("helloo"))
print(tuple([1,2,3,4,5,6]))


print("\ntype함수 ===")
# 입력밧이 자료형이 무엇인지 알려주는 함수 
print("3의 자료형 타입 => ", type(3))
print("[1,2,3,4]의 자료형 타입 => ", type([1,2,3,4]))
print("'jjisoo'의 자료형 타입 => ", type('jjisoo'))


print("\nzip함수 ===")
#동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다.
a = list(zip([1,2,3], [4,5,6]))
print(a)
b = list(zip('abc', 'def'))
print(b)