# while문


# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요:  "))  #input  함수 == 자바의 스캐너객체와 같은 역할 임
#     if money == 300:
#         print("커피를 줍니다")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("금액이 부족합니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다")
#         break

# 1 부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해보자.
a = 0
while a < 10:
    a = a+1
    if a % 3 == 0:
        continue
    print(a)

# for 문
print("\n===============for문 예제==================\n")
a = [(1, 2), (3, 4), (5, 6)]
for (a, b) in a:
    print(a+b)


print("\n===============for문 예제2==================\n")
marks = [90, 30, 60, 70, 75]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


print("\n--------------------------range  함수--------------------------\n")
add = 0
for i in range(1, 11):  # 1 부터 10까지 돌기
    add = add + i

print(add)

print("\n-------------------------리스트 내포 --------------------------\n")

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*2)
print(result)

print("\n-------------------------리스트 내포 --------------------------\n")
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

print("\n-------------------------for문 테스트 -------------------------\n")

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

print("\n-------------------------for문 테스트 -------------------------\n")
i = 0
while True:
    i = i + 1
    if i > 5:
        break
    print(i * "*")

print("\n-------------------------for문 테스트 -------------------------\n")
for i in range(1, 101):
    print(i)

print("\n-------------------------for문 테스트 -------------------------\n")
# A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

print("\n-------------------------for문 테스트 -------------------------\n")

number = [1, 2, 3, 4, 5]
result = [n * 2 for n in number if n % 2 == 1]
print(result)
