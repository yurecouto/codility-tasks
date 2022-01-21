def solution(A, K):
    for i in range(0, K):       # esse loope irá fazer K rotações ciclicas em A
        if A == []:             # checa se a lista estiver vazia
            return A            # retorna a lista caso seja vazia
                        
        A.insert(0, A.pop())    # insere no primeiro indice de A o ultimo elemento de A
        
    return A                    # retorna A após as rotações K

test = [1, 2, 3, 4]

print(solution(test, 3))
