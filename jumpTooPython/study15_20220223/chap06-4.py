# chap 06-4 게시판 페이징하기
import sys

option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]  # 메모한 내용
    f = open(
        "C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study15_20220223/memo.txt", 'a')
    f.write(memo)
    f.write("\n")
    f.close()
elif option == '-v':
    f = open(
        "C:/Users/sdh20/Desktop/pythonWeb/jumpTooPython/study15_20220223/memo.txt")
    memo = f.read()
    f.close()
    print(memo)
