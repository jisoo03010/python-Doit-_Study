# chap 06-5.py
# 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("0", " ")

f = open(dst, 'w')
f.write(space_content)
f.close()
