# chap 07-3 강력한 정규 표현식의 세계로
# " | " => or과 동일한 의미로 사용된다.
from itertools import count
import re
p = re.compile("Crow|Servo")  # Crow 또는 Servo가 같은게 있나?
m = p.match('CrowHello')  # Crow 또는 Servo 중 하나라도 매치가 된다면 출력하라라는 비스무리한..뜻
print(m)


# " ^ " => 문자열의 맨 처음과 일치함을 의미한다.
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'my Life'))
print("\n")
# " $ " => 문자열의 맨 끝과 일치함을 의미한다. ^과 반대의 경우
print(re.search('Life$', 'Life is too short'))
print(re.search('Life$', 'my Life'))
print("\n")
print("\n\A  =======")
# " \A " => 문자열의 처음과 매치됨을 의미한다 .
# ^메타 문자와 동일한 의미이지만 re.MULTILINE옵션을 사용할 경우에는 다르게 해석된다
# \A는 줄과 상관없이 전체 물자열의 처음하고만 매치한다
print("\n\Z =======")

# " \Z " => $과 달리 전체 문자열의 끝과 매치됨을 의미한다 .
print("\n b =======")
# \b 는 단어 구분자이다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  # class라는 단어와 매치됨을 확인할 수 있다.
print(p.search('noclass at all'))  # noclass에 class가 있긴하지만 구분되어 있지 않아 매치되지 않는다.

print("\n B =======")
# \B 베타문자는 \b 메타 문자와 반대의 경우이다.
# 구분된 단어가 아닌경우에만 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('noclass at all'))  # class 단어 뒤에 whitespace 가 있어서 매치가 되지 않는다.
print(p.search('noclassno at all'))  # 앞뒤에 whitespace가 하나도 없어야 매치되는걸 볼 수 있다.


print("그루핑!!!==============================")
# ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다면?
# (ABC)+ 다음처럼 그루핑을 사용하여 작성 할 수 있다.
p = re.compile("(ABC)+")
m = p.search('ABCABCABC OK?')
print(m)

# 그룹을 만들어 주는 메타문자는 바로 ( ) dlek.
print(m.group(0))


p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("pack 010-9968-7835")
print(m)

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("pack 010-9968-7835")
print(m.group(1))

print("\n그루핑 된 문자열 재참조하기=========")
# 그루핑 된 문자열 재참조하기
p = re.compile(r'(\b\w+)\s+\1')
m = p.search("Paris in the the spring").group()
# \1 => 그룹과 동일한 언어와 매치됨을 의미한다.
print(m)


print("\n그루핑 문자열 이름 붙이기=========")
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("kim 010-9968-7835")
print(m.group("name"))


print("\n전방탐색=========")
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# 긍정형 전방탐색 => (?=...)
# 부정형 전방탐색 => (?!=...)

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

print("\n문자열 바꾸기=========")
p = re.compile("(blue|white|red)")
# 첫 번째 매개변수는 바꿀 문자열이 되고
# 두 번쨰 매개변수는 대상 문자열이 된다.
m = p.sub("colour", "blue socks and red shoes")
print(m)

m = p.sub("colour", "blue socks and red shoes", count=1)
print(m)
