print("\nfilter함수 ===")
#첫 번째 인수로 함수의 이름
#두 번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다.
#두 번째 인수인 반복 가능한 잘형 요소가 첫 번째 인수인 함수에 입력되었을때 반환 값이 참인 것만 묶어서 돌려준다.
def positive(l):
    result = []
    for i in l:
        if i > 0: #i 가 0보다 큰걸 걸러내어 result에 i를 추가한다.
            result.append(i) 
    return result
print(positive([1, -3, 2, 0, -5, 6]))

#filter 함수를 사용하면 좀더 간단하다 아래를 참고
def positive(x):
    return x > 0
print(tuple(filter(positive, [1, -3, 2, 0, -5, 6]))) #걸러낸 값을 튜플 tuple 로 받음 
print("\n ====== 더 간단해지는 방법 lambda")
print(list(filter(lambda x : x > 0, [1, -3, 2, 0, -5, 6])))

