# 문자열 관련 함수


# 문자 개수 count
a = "hobby"
print(a.count('b'))  # b의 문자가 2개 있음

# 위치 알려주는 함수 find
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # a가 k를 포함하고 있지않으므로 -1을 반환

# 위치 알려주는 함수2
a = "Life is too short"
print(a.index('i'))

# 문자열 삽입 join
print(",".join('abcdefg'))  # 문자열의 각각의 사이에 ' , '를 삽입

# 소문자 대문자 변경
upper = "hello"
print(upper.upper())
lower = "HELLO"
print(lower.lower())


# 왼쪽 공백 제거 lstrip
a = "    hi  d"
print(a.lstrip())
# 오른쪽 공백 제거 rstrip
a = "          hi                    "
print(a.rstrip())

# 양쪽 공백 모두 지우기
print(a.strip())

# 문자열 변경 replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 split
a = "Life is too short"
print(a.split())  # 공백을 기준으로 문자열 나눔
print(a.split(":"))  # 기호를 기준으로 문자열 나눔
