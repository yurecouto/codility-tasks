def solution(A, K):
    for k in range(K):
        if A == []:
            return A
        
        A.insert(0, A.pop())
        
    return A
    
test = [1, 2]

print(solution(test, 1))