# 리스트 자료형
a = [3, 4, 5, 6, 7, 8, 9]
print(len(a))

a[0] = 1
print(a)

# 요소 삭제
del a[0]
print(a)

# 요소 추가
a.append(10)
print(a)

a.append([1, 2, 3])
print(a)

# 리스트 정렬
a = [1, 4, 5, 3, 2]
a.sort()
print(a)

# 리스트 뒤집기
a.reverse()
print(a)


# 리스트 요소 삽입 insert
a = [1, 2, 3]
a.insert(3, 4)  # 리스트 3번 위치에 4요소 추가
print(a)

a.remove(1)  # a리스트의 요소 1제거
print(a)

b = [0, 1, 2, 3, 4, 5, 6, 7]
b.pop()  # 마지막 요소 끄집어내기 (마지막 요소 삭제됨)
print(b)

b.pop(3)  # 3요소 삭제
print(b)

print(b)

print(b.count(2))  # 요소 2가 리스트안에 몇개 있는지 확인

# 리스트 확장 extend
a = [1, 2, 3]
b = [4, 5, 6]

# a리스트에 b리스트를 더하게 된다.
a.extend(b)
print("a리스트 + b리스트 = ", a)
