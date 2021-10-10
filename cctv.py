import os
os.system('cls')

def solution(routes):
    routes.sort(key = lambda x : (x[0], x[1]))

    left, right, answer = routes[0][0], routes[0][1], 1

    for route in routes[1:] :
        if left <= route[0] and right >= route[0] :
            left = route[0]
            right = min(right, route[1])
        else :
            left, right = route[0], route[1]
            answer += 1
    return answer

print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18, -14], [-18,-13], [-5,-3]]), 2)
