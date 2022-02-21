# 컴퓨터에서 동작하고 있는 프로그램 = 프로세스라고 부른다
# 보통 1개의 프로세스는 한 가지 일만 하지만
# 스레드 (thread)를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

# import time

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# for i in range(5): #long_task를 5회 수행한다.
#     long_task()

# print("End")



# import time
# import threading

# def long_task():
#     for i in range(1, 6):
#         time.sleep(1)
#         print("working:%s\n" % i)
# print("Start")

# threads =[]
# for i in range(5): #long_task를 5회 수행한다.
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()

# print("End")
# 위의 코드를 실행하면 start, end가 먼저 실행된후 스레드가 순차적으로 실행된다. 그리고 정상 종료되지 않는다.
# 우리가 기대하는 것은 Start가 먼저 출력되고 그 다음에 스레드의 결과가 출력된 후 마지막으로 end가 출력되는 것이다

#이 문제를 해결하기 위해서는 다음과 같이 프로그램을 수정해야 한다.

import time
import threading

def long_task():
    for i in range(1, 6):
        time.sleep(1)
        print("working:%s\n" % i)
print("Start")

threads =[]
for i in range(5): #long_task를 5회 수행한다.
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start() # 스레드 실행
    
# join 을 추가하여 join으로 스레드가 종료될 때까지 기다린다.
for t in threads:
    t.join() # join함수는 해당 스레드가 종료될 때까지 기다리게 한다.

print("End")