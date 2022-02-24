# 정규 표현식
# 메타 문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.
# 문자 클래스 => [ ]
#  [ ] => 사이의 문자들과 매칭 , ex) [abc] => a, b, c중 한개의 문자와 매치를 뜻한다.
# " - " => 범위
# [a-zA-Z] => 알파벳 모두
# [0-9] => 숫자 모두
# " ^ " => 반대라는 의미 ex) [^0-9] => 숫자가 아닌 문자만 매칭된다.

# " . " => 온점은 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미
# ex) a.b => a와 b사이엔 모든 문자가 들어가도 매칭된다
# ex ) a[.]b => 모든 문자가 아닌 문자만 매칭된다

# 반복(*) => ex ) ca*t : 문자 바로앞에 있는 a가 0번 이상 반복되면 매칭
# ct : yes ?? 0번 이상 반복되어 yes
# cat : yes
# caaaat : yes

# 반복( + ) => 반복을 나타내는 또다른 메타 문자로 + 가 있는데
# +는 최소 1번 이상 반복될 때 사용한다. 즉 * 가 반복횟수 0번 부터라면 + 는 반복횟수가 1부터인 것이다.

# 반복({m, n} , ?) => {m, n} : 반복횟구를 고정할 수 있다. m에서 n까지 만 반복
#  m, n은 생략 가능
# {3, } => 3 이상
# {, 3} => 3 이하
# {1, } => +와 동일,, {0, } => *와 동일하다.

# {m}
# ca{2}t => "c + a(반드시 2번 반복) +t"
# cat : no
# caat : yes


# {m, n}
# ca{2, 5}t => "c + a(반드시 2번 ~ 5번 반복) +t"
# cat : no
# caat : yes
# caaaat : yes
# caaaaat : yes

# ? => 있어도 되고 없어도 된다.
# ? 가 의미하는것은 {0, 1}이다.
# ex ) ab?c => "a +b(있어도 되고 없어도 된다) + c"
# abc : yes
# ac : yes


import re
print("\n re.compile =====")
p = re.compile('[a-z]+')  # 정규 표현식을 컴파일 해준다

print("\n p.match =====")
# 정규식을 사용한 문자열 검색
m = p.match("abb")  # 매칭되어 match 객체를 돌려준다.
print(m)

x = p.match("3cc")  # 매칭되지 않아 None값을 돌려줌
print(x)

print("\n p.search =====")
m = p.search("python")  # match 메서드를 수행했을 때와 동일하게 매치된다.
print(m)

m = p.search("3 python")
# 앞에 숫자 3이 있는데도 불구하고 매치된다고 하는 이유?
#  search 함수는 문자열 전체를 검사하기 때문에
# 3이후의 python 문자열과 매치된다고 한것이다
print(m)

print("\n p.findall =====")
result = p.findall("life is too short")
# 정규식과 매칭되는 모든 문자열을 리스트로 돌려준다.
print(result)

print("\n p.finditer =====")
result = p.finditer("life is too short")
print(result)

for r in result:
    print(r)

print("\n match객체의 메서드 =====")

m = p.match("python")

print("m.group() =>", m.group())

print("m.start() =>", m.start())
print("m.end() =>", m.end())
print("m.span() =>", m.span())
print("\n\n\n search 메서드========")
s = p.search("33python")
print("s.group() =>", s.group())

print("s.start() =>", s.start())
print("s.end() =>", s.end())
print("s.span() =>", s.span())
