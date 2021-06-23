# 6월 23일
# 백준 1935번

import sys

nums, ans = [], []

n = int(sys.stdin.readline())  # 몇개의 숫자인지

command = sys.stdin.readline().strip()  # 후위표기식

for _ in range(n):
    nums.append(int(sys.stdin.readline()))  # 숫자부분 모으기

for one in command:
    if one.isupper():  # 대문자이면
        ans.append(nums[ord(one) - ord('A')])  # 문자를 숫자로

    else:
        num2 = ans.pop()
        num1 = ans.pop()
        if one == '+':
            ans.append(num1 + num2)
        elif one == '-':
            ans.append(num1 - num2)
        elif one == '/':
            ans.append(num1 / num2)
        elif one == '*':
            ans.append(num1 * num2)

print(f"{ans[0]:.2f}")
