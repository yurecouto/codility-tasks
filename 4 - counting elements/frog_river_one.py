def solution(X, A):
    # creating the steps the frog should make
    steps = set([i for i in range(1, X + 1)])

    # creating the steps the frog already did
    frog_steps = set()

    for index, leaf in enumerate(A):
        frog_steps.add(leaf)
        if frog_steps == steps:
            return index
    return -1

        

A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

print(solution(X, A))