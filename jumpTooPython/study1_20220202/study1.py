# 파이썬 주석을 여러 줄 적상하려면

"""
Author: EungYong Park
Date : 2019-05-01
이 프로그램은 Hello World를 출력하는 프로그램이다.
"""

'''
Author: EungYong Park
Date : 2019-05-01
이 프로그램은 Hello World를 출력하는 프로그램이다.
'''
# 파이썬  문자열 출력


print("\n")
food = "Python's favorite food is perlf"
print(food)
print("\n")

multiline = """
... Life is too short
... You need python
"""
print(multiline)


# 문자열의 길이 구하기
a = "You need python"
print(a)
print(len(a))

# 문자열 인덱싱
print("a의 4번째 문자 ? \n "+a[4])

# 문자열 포매팅 따라하기

# 1. 숫자 대입
print("I eat { %d  } apples." % 3)

# 2. 문자열 바로 대입
print("I eat { %s } apples." % "five")

# 3. 숫자 값을 나타내는 변수로 대입
number = 19
print("my age : { %d }" % number)

# 2개 이상의 값 넣기
number = 10
day = "three"

print("I ate { %d }apples. so  I was sick for { %s } days." % (number, day))

print("%10s" % "hi")
# %10s : 전체 길이가 10개인 문자열 공간에서  대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백을 남겨 두라는 의미이다.

print("%-10shi" % "jisoo")

#  format 함수를 사용한 포매팅
print("I eat {0} apples.".format(4))
print("I eat {0} apples.".format("five"))

#  format 함수를 사용한 1개 이상의 포매팅
print("I eat ( {0} ) apples. so I was sick for ( {1} ) days.".format(4, "five"))

# format 함수를 이용한 이름으로 값 넣기
print(
    "I eat ( {number} ) apples. so I was sick for ( {day} ) days.".format(number=49, day="five"))


print("\n =========================파이썬 정렬======================= ")
# 파이썬 정렬
print("{0:<10}jisoo".format("hi\n"))  # hi 를 왼쪽 정렬

print("{0:>10}hi".format("jisoo\n"))  # jisoo를 오른쪽 정렬

print("{0:^10}".format("jisoo\n"))  # jisoo를 가운데 정렬

# 공백 채우기
print("{0:=^10}".format("hi"))

# f 문자열 포매팅
age = 19
print(f"내년이면 { age + 1}살이 된다.")

d = {'name': '홍길동', 'age': 30}

print(f'나의 이름은{d["name"]}이고,  나이는 {d["age"]}입니다.')

# f문자열 포매팅 정렬 방법
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')


print(f'{"hi":=^10}')


y = 3.141592
print(f'{y:0.4f}')

# 자릿수 전체 10으로 소숫점은 4자리 까지만
print(f'{y:10.4f}')


print("{0:!^12}".format("python"))
print(f'{"python":!^12}')
