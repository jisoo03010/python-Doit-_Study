# 클래스 변수 
class Family:
    lastname = "김"

print("\n\n\n=====클래스 변수 ======\n")
print(Family.lastname)

print("\nj === family클래스로 만든 객체를 통해서 클래스 변수 가져오기=====\n")
a = Family()

print(a.lastname)

a.lastname = "박"
print(a.lastname) # lastname이 "박" 으로 바뀜

print("\n\n\n==id 함수 사용해서 메모리 같은지 안같은지 확인하기 =\n")
print(id(Family.lastname))

print(id(a.lastname))