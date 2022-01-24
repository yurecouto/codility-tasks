def solution(A):
    head = A[0]                             
    tail = sum(A[1:])
    min_dif = abs(head - tail)              # Define as partes e testa suas diferenças
                                                    
    for index in range(1, len(A) - 1):      # Esta parte testa todas as diferenças entre as duas partes
        head += A[index]                    
        tail -= A[index]
        if abs(head - tail) < min_dif:
            min_dif = abs(head - tail)
            
    return min_dif


A = [3, 1, 2, 4, 3]

print(solution(A))
