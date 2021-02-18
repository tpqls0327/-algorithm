# 무지의 먹방 라이브

# 시간에서 에러가 발생함/ 힙을 공부한후 다시 풀기
def solution(food_times, k):
    answer = 0
    
    cnt = 0
    while True:
        if cnt == k:
            break
        answer = answer % 3
        
        if food_times[answer] != 0:
            food_times[answer] -= 1
            cnt += 1
            answer += 1
            print(food_times, cnt, answer)
        else:
            answer += 1
    
    cnt = 0
    for i in range(len(food_times)):
        answer = answer % 3
        
        if food_times[answer] != 0:
            answer += 1
            break
        answer += 1
        cnt += 1
        if cnt == sum(food_times):
            answer = -1        
    return answer

print(solution([3,1,2], 5))
