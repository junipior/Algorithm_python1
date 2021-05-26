# 5월 22일
# 백준 1874번

import sys

cnt, stack, result, no = 1, [], [], True

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    while cnt <= x:
        stack.append(cnt)
        result.append("+")
        cnt += 1

    if stack[-1] == x:
        stack.pop()
        result.append("-")

    else:
        no = False
        break

if no == False:
    print("NO")
else:
    print("\n".join(result))
