# OS 모듈
# => 환경 변수나, 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈이다.

#환경 변수? 

#내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ
#  os.environ => 현재 시스템의 환경 변수 값을 보여준다.
import os 
print(os.environ) # 필자의 시스템 정보
print("\n\n\n\n\n\n\n")
print(os.environ['PATH']) # 필자 시스템의 PATH 환경 변수 내용이다.
print("\n\n\n\n\n\n\n")
#디렉터리 위치 변경하기
print(os.chdir("C:\WINDOWS"))

#디렉터리 위치 돌려받기 
print("디렉터리 위치 돌려받기 ", os.getcwd())


#시스템 명령어 호출하기 - os.systems
print(os.system("dir")) # dir열기
print("\n\nos.popen=======\n\n")
#실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# => 시스템 명령어를 실행한 결괏값을 일기 모드 형태의 파일 객체로 돌려준다.
f = os.popen("dir")
print(f.read())

#기타 유용한 os 관련 함수

"""
os.mkdir(디렉터리) => 디렉터리 생성
os.rmdir(디렉터리) => 디렉터리를 삭제한다. (단 디렉터리가 비어 있어야 삭제가 가능하다.)
os.unlink(파일이름) => 파일을 지운다.
os.rename(src, dst) => src라는 이름의 파일을 dst라는 이름으로 바꾼다.






"""