#try ... finally
# => 보통 finally절은 사용한 리소스를  close 해야 할때에 많이 사용된다.
f = open('foo.txt', 'w')
try :
    print(2)
finally:
    f.close()
print("\n========")
#여러개의 오류 처리하기
try:
    a= [1,2]
    print(a[3])
    4 / 0
except IndexError:
    print("인덱싱할 수 없습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 결과 : "인덱싱할 수 없습니다." 
# "0으로 나눌 수 없습니다." 가 나오지 않는 이유?
# => 인덱싱 오류가 먼저 발생했으므로 4/ 0으로 발생되는 seroDicisionError오류는 발생하지 않았다.,

print("\n==2번째 방법 ======")
try:
    a= [1,2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


print("\n== 2개 이상의 오류 동시에 처리하기 ======")
try:
    a= [1,2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#########오류 피하기  ########
try:
    f = open("나없는 파일", 'r')
except FileNotFoundError:
    pass  # 파일이 없더랃도 오류를 발생시키지 않고 통과한다 

########## 오류 일부러 발생시키기 ###########
print("\n########오류 일부러 발생시키기########\n")
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird): #Eagle클래스는 Bird클래스를 상속받는다.
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

#예외 만들기
print("\n\n\n ========= 예외 만들기  ==========\n")

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 벌명입니다."

#별명을 출력해 주는 함수 
def say_nick(nick):
    if nick == "바보": # 만약에 입력받은  nick의 값이 "바보"면 MyError클래스에 일부로 에러나게 하기 
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

# 오류 메시지를 사용하고 싶다면 아래처럼 해야한다.
print("\n=======오류 메시지를 사용하고 싶다면 아래처럼 해야한다======.")
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)