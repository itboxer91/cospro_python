# 코스프로 파이썬 2급_3차
'''
리스트 오름차순/내림차순
scores.sort(reverse=False) : 디폴트 오름차순
scores.sort(reverse=True) : 내림차순
'''
def func_a(scores, score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def func_b(arr):
    arr.sort(reverse=True)

def func_c(arr, n):
    return arr[n]

def solution(scores, n):
    score = func_c(scores, n) #3번 학생의 점수를 파악
    func_b(scores) #점수 리스트에 대한 내림차순 정렬
    answer = func_a(scores,score)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59]
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")