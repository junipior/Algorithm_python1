# 6월 3일
# 프로그래머스 스택/큐
# 프린터
# any, enumrate 활용

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)] # (인덱스, priorities)를 순서대로 리스트에 담음
    answer = 0
    while True: # 무한 루프
        cur = queue.pop(0) # 반복문이 아니라 한번만 실행할 경우 첫번 쨰 (i,p) 값만 cur에 할당
        if any(cur[1] < q[1] for q in queue): # cur[1]가 가장 큰수가 아닐 경우/ cf. cur[0]은 인덱스에 해당
            queue.append(cur)
        else: # cur[1]가 가장 큰수일 경우
            answer += 1
            if cur[0] == location:
                return answer # return을 만나 무한 루프 종료


solution([2, 1, 3, 2], 2)