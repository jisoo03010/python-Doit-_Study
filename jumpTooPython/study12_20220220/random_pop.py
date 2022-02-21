# 모듈을 이용한 재미있는 함수 만들기
import numbers
import random
from unicodedata import numeric
def random_pop(data):
    number = random.randint(0, len(data) -1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))

print("\n\n\n\n\n random.choice함수를 하용하여 좀더 직관적으로 만들 수 있다. =====")
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))



print("\n\n 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle함수를 사용 =====")
data = [1,2,3,4,5 ]
random.shuffle(data) # 데이터를 무작위로 섞음
print(data)


