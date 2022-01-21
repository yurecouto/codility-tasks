def solution(N):
    binary = bin(N).replace('0b', '')
    ones = []
    gaps = []

    for i in range(len(binary)):            # Esse loop separa os numeros '1' por suas posições                            
        if binary[i] == '1':                # e a partir dessas posições é possível ver o tamanho dos gaps
            ones.append(i)

    for j in range(len(ones) - 1):          # Agora a ideia é subtrair as posições, a primeira e a segunda, a segunda e a terceira...
        gap = ones[j + 1] - (ones[j] + 1)   # isso irá retornar o tamanho do gap.

        gaps.append(gap)

    if gaps == []:
        return 0

    else:
        return max(gaps)
        

solution(1041)