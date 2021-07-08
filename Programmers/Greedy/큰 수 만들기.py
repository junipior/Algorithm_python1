# 7월 8일
# 프로그래머스 그리디(Greedy)

def solution(number, k):
    stack = []
    for i in number:
        while stack and i > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    if k > 0:
        for _ in range(k):
            stack.pop()

    answer = "".join(stack)
    return answer

# input
# solution("4177252841", 4)

# output
# "775841"