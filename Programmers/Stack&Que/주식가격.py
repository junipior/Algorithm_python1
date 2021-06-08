# 6월 7일
# 프로그래머스 스택/큐
# 주식 가격

def solution(p):
    ans = [0] * len(p)
    stack = [0]					# 결정이 안 된 요소의 인자 번호들
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:			# 감소가 일어났을 때
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j		# ans 값을 결정
                    stack.remove(j)		# 결정된 값은 stack에서 제거
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans