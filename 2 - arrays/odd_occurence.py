def solution(A):                
    result = 0                  # Esso foi um dos que mais me deu trabalho, simplesmete pois não tinha
    for i in A:                 # ideia de como fazer funcionar, isso pois não conhecia esse operador
        result ^= i             # "^" e sinceramente não sei o que ele faz
    return result

A = [9, 3, 9, 3, 9, 7, 9]

print(solution(A))

