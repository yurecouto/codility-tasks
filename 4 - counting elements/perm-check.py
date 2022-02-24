def solution(A):
    A.sort()

    if A[-1] != len(A):
        return 0

    else:
        if A[0] != 1:
            return 0
            
        return 1