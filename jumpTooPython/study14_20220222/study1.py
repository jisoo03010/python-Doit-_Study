# 구구단 프로그램
from unittest import result


def gugu(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result


print("\n\n")
print(gugu(2))
