# python 연습 문제

from dataclasses import replace


print("\n==========문제 1번======\n")
def is_odd(number):
    if number % 2 == 1 :
        return True
    else:
        return False

print(is_odd(2))
print(is_odd(3))


print("\n==========문제 2번======\n")

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2,3,4,5,6))


print("\n==========문제 3번======\n")
result1 = input("첫번째 숫자를 입력하세요 : ")
result2 = input("번번째 숫자를 입력하세요 : ")
total = int(result1)  + int(result2) 

print("두수의 합은 %d입니다." %total)

print("\n==========문제 5번======\n")
f = open("C:/Users/sdh20/test.txt", 'w')
f.write("Life is too short")
f.close()

print("\n==========문제 6번======\n")
user_input = input("저장할 내용을 입력하세요 : ")
f = open("C:/Users/sdh20/test.txt", 'a')
f.write(user_input)
f.write("\n")
f.close()


print("\n==========문제 7번======\n")

f =  open("C:/Users/sdh20/test.txt", 'r')
body = "Life is too short\n you need java"
f.close()

body = body.replace('java', 'python')
f =  open("C:/Users/sdh20/test.txt", 'w')
f.write(body)
f.close()