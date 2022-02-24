# 컴파일 옵션
# 정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.
"""
옵션 이름 
DOTALL
IGNORECASE
MULTILINE
VERBOSE
"""
import re
m = re.match("a.b", "a\nb")
print(m)

# \n도 매치하고 싶다면 re.DOTALL 또는 re.S를 사용해 정규식을 컴파일하면 된다.
p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)

print("\n\nIGNORECASE====")
# IGNORECASE, I => 대 소문자 구별없이 매치를 수행할 때 사용하는 옵션이다.
p = re.compile("[a-z]", re.I)
m = p.match("python")
print(m)
m = p.match("PYTHON")
print(m)


print("\n\nMULTILINE====")
# ^ => 문자열의 처음을 의미, $ => 문자열의 끝을 의미
# ex) ^python 문자열의 처음은 항상 python으로 시작해야함
# ex) $python 문자열의 끝 항상 python으로 끝나야함

# python 으로 시작하고 그 뒤에 단어가 와야한다는 의미이다.
p = re.compile("^python\s\w+", re.M)
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # fnindall => 매치되는 값을 리스트로 돌려줌

print("\n\nVERBOSE, X====")
# 어려운 정규식을 주석 또는 줄 단위로 구분할 수 있ㅎ다면 얼마나 보기 좋고 이해하기 쉬울까?
# 방법이 있다. verbose 를 사용하는 것
