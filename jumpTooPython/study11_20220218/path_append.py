import sys
sys.path.append("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study11_20220218")

# pickle => 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

import pickle
f = open("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study11_20220218/test.txt", 'wb')
data = {1 : 'python', 2: 'you need'}
pickle.dump(data, f) #pickle.dump() 를 사용해서 data를 그대로 파일에 저장하는 방법을 보여줌
f.close()


import pickle
f = open("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study11_20220218/test.txt", 'rb')
data = pickle.load(f) # pickle.load(를 사용해서 원래 있던 딕셔너리 객체 상태 그대로 불러오는 예이다.
print(data)