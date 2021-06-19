# 6월 19일
# Implementation
# p.113

# H 입력 받기
H = int(input())

count = 0
for i in range(H + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)