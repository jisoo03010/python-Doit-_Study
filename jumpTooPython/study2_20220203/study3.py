# 튜플 자료형
"""
리스트와 튜플의 차이점
리스트는 (수정, 삭제, 변경)이 가능하지만, 튜플은 모두되지 않는다.
그런 점만 제외하면 리스트와 다름 없다.

튜플은 한개의 요소만 넣을 경우 맨위 쉼표를 넣어줘야 한다.

t1 = (1,)

"""
print("\n")
# 튜플 다루기

t1 = (1, 2, 'a', 'b')
print(t1[0])
t2 = (3, 4, 'c', 'd')
print(t1 + t2)

# 튜플 곱하기
print(t2 * 3)
print(len(t2))


# 딕셔너리 자료형
# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a['jisoo'] = 'c'
a[4] = 'd'
print(a)


# 튜플 요소 삭제하기
del a[2]
print(a, "\n")

# 딕셔너리 key사용해서 value값 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])


# 딕셔너리 관련함수
print(grade.keys(), "\n")

a = {'name': 'jisoo', 'phone': '01099687835', 'birth': '040310'}
for k in a.keys():
    print(k)

print(list(a.keys()))

# value 리스트 만들기
print("values : ", a.values(), "\n")
# key : values 쌍 얻기
print("\n items() 함수\n\n")
print(a.items(), "\n")

# key로 value얻는 함수 get함수

a = {'name': 'jisoo', 'phone': '01099687835', 'birth': '040310'}
print(a.get('name'))


# key가 없을 경우 미리 정해둔 이폴트 값을 대신 가져오기
print(a.get('foo', 'none'))

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in a)
