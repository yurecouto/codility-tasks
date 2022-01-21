def solution(A):
    B = sorted(A)
        
    if len(B) == 1:
        x = B[0] + 1
        return x

    if len(B) > 1:
        for n in range(0, len(B) + 1):
            if B[n] != n + 1:
                x = n + 1
                return x

                           
a = [1]

print(solution(a))