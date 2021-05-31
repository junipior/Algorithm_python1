# 5월 31일
# 프로그래머스 스택/큐
# 기능개발

def solution(progresses, speeds):
    day, answer = [], []
    for i, j in zip(progresses, speeds):
        if (100 - i) % j == 0:
            day.append((100 - i) // j)
        else:
            day.append(((100 - i) // j) + 1)

    # count를 제거하고 리스트에 직접 카운트하는 방식 + enumerate 사용
    for i, d in enumerate(day):
        # 초기값을 max값으로 세팅
        if i == 0:
            max = d
            answer.append(1)
            continue

            # max보다 시간이 더적게걸린다면 이전값 +1 (리스트 [-1] 사용)
        if d <= max:
            answer[-1] += 1

            # 현재값이 max라면 max를 갱신하고 answer요소를 새로 추가
        else:
            max = d
            answer.append(1)

    return answer