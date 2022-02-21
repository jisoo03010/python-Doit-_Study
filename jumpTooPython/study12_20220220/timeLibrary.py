from cgi import print_directory
import time
from traceback import print_tb
print("\n time.strftime==========")
# time.strftime(' 출력할 형식 포맷 코드', time.localtime(time.time()))

print(time.strftime('%x', time.localtime(time.time()))) # 현재 설정된 지역에 기반한 시간 출력
print(time.strftime('%c', time.localtime(time.time()))) # 날짜와 시간을 출력함

print("\n time.sleep==========")
# 일정한 시간 간격을 두고 루프를 실행할 수 있다.
for i in range(10):
    print(i)
    time.sleep(0.1) # 1초마다 i를 출력한다.
    
print("\n calendar==========")
# 파이썬에서 달려을 볼 수 있게 해주는 모듈이다.
import calendar
#메모장에 달려만듦
f = open("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study12_20220220/src.txt", 'w')
f.write(calendar.calendar(2022))
f.close()
print("\n\n")
print("\n calendar.calendar==========")
print(calendar.calendar(2022))

print("\n\n\n calendar.prcal==========")
print(calendar.prcal(2022)) # calendar.calendar(2022) == calendar.prcal(2022) 같은 결과 나옴


print("\n\n\n calendar.prmonth==========")
print(calendar.prmonth(2022, 1)) # 2022년도의 1월달 달력만 보여줌


print("\n\n\n calendar.weekday==========")
# 0 => 월요일
# 1 => 화요일
# 2 => 수요일
# 3 => 목요일
# 4 => 금요일
# 5 => 토요일
# 6 => 일요일
print( "%d요일 " %calendar.weekday(2022, 2, 21))


print("\n\n\n calendar.monthrange==========")
# 연도와 월을 입력받아 입력받은 달의 1일이 무슨 요일인지, 
# # 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
print(calendar.monthrange(2022, 1)) #1일은 토요일, 마지막 일자는 31일까지 있음





















































































































































































































