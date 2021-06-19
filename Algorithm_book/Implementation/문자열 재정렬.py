# 6월 19일
# Implementation
# p.113

ip = input()
num = 0
result = []

for i in ip:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자를 맨 뒤로
if num != 0:
    result.append(str(num))

# 하나로 합치 (리스트를 문자열로 출력)
print(''.join(result))

# input
# K1KA5CB7
# AJKDLSI412K4JSJ9D

# output
# ABCKK13
# ADDIJJJKKLSS20