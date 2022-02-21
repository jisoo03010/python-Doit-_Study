#
print("\n shutil==========")
#파일을 복사해주는 파이썬 모듈
from cgi import print_directory
import shutil
shutil.copy("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study12_20220220/src.txt", "C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study12_20220220/dst.txt")


#glob

print("\n glob==========")
# => 디렉터리에 있는 파일들을 리스트로 만들기
#  *, ? 등 메타 문자를 사용해서 원하는 파일만 읽어 들일 수 있다.

#ex) mark로 시작하는 파일을 모두 찾아서 읽어들이는 예제
import glob
print(glob.glob("C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study12_20220220/mark*"))



print("\n tempfile==========")
# 파일을 임시로 만들어서 사용할때 유용한 모듈이다.
#tempfile.mkstemp() => 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
import tempfile
filename = tempfile.mkstemp()
print(filename)

#tempfile.TemporaryFile()은 => 임시 저장공간으로 사용할 파일 객체를 돌려준다.
# 이파일은 기본적으로 바이너리 쓰기 모드 값을 갖는다. f.close가 호출되면 이 파일 객체는 자동으로 사라진다.
import tempfile
f = tempfile.TemporaryFile()
f.close()

#시간과 관련된 time 모듈

print("\n time==========")
import time
print("\n time.time==========")
print(time.time()) #현재 시간을 실수 행태로 돌려주며 시간을 초 단위로 알려준다.

print("\n time.localtime==========")
print(time.localtime()) # 돌려준 실수값을 사용해서 연도, 월, 일, 시, 분, 초 -- 의 형태로 바꾸어주는 함수

print("\n time.asctime==========")
# time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
print(time.asctime(time.localtime(time.time())))

print("\n time.ctime==========")
#time.asctime(time.localtime(time.time())) => time.ctiem()을 사용해서 간편하게 표실할 수 있다,.\
# asctime과 다른점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
print(time.ctime())
























































