# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 1
    count = 0
    num = []

    while answer <= n:  # 1 ~ n회차
        for i in range(2, answer + 2):
            for j in range(1, i):
                if i % j == 0:
                    count += 1

                if count == 2:
                    count = 0
                    num.append(i)

        answer += 1  # n까지 증가

    return len(num)

# while 문으로 해 보려다 개같이 멸망


print(solution(10))  # 4 [2, 3, 5, 7]
print(solution(5))  # 3 [2, 3, 5]
