def solution(A):
    B = sorted(A)
    b = len(B)

    if b == 0:
        return 1
    
    elif b == 1:
        if B[0] == 1:
            return B[0] + 1

        elif B[0] != 1:
            return 1

    elif b == B[-1]:
        return b + 1

    elif b >= 1:
        if B[0] != 1:
            return 1

        for n in range(0, b + 1):
            if B[n] != n + 1:
                return n + 1
                          

a = [1, 2]

print(solution(a))
