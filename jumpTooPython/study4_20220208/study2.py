#사용자 입력과 출력 
#input 사용
# a = input("입력하시오 : ")
#print(a)

for i in range(10):
    print(i, end=' ')

print("\n")
print("\n========파일 읽고 쓰기=========\n")
f = open("C:/Users/sdh20/doit.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print("\n")
#프로그램의 외부에 저장된 파일을 읽어오는 여러가지 방법
print("\n\n========readline===========")
# f = open("C:/Users/sdh20/doit.txt", 'r')
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close()

# print("\n")

# while 1:
#     data = input()
#     if not data : break
#     print(data)


print("\n 파일 읽어오기 =====================")
f = open("C:/Users/sdh20/doit.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)


print("\n======read 함수======== \n")
f = open("C:/Users/sdh20/doit.txt", 'r')
data = f.read() # 파일의 내용 전체를 문자열로 돌려준다.
print(data)
f.close()


# 파일에 새로운 내용 추가하기( a ) 

f = open("C:/Users/sdh20/doit.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다\n" % i
    f.write(data)
f.close()

# with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리함 
with open("C:/Users/sdh20/doit.txt", 'a') as f:
    f.write("Life is too short, you need python")

print("\n===sys 모듈======\n")

import sys

args = sys.argv[1:]
for i in args:
    print(i)