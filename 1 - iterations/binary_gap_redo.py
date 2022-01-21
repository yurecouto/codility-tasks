def solution(N):
    binary = bin(N).replace('0b', '')
    ones = []
    gaps = []
    
    for i in range(len(binary)):
        if binary[i] == '1':
            ones.append(i)
            
    for j in range(len(ones) - 1):
        gap = ones[j + 1] - ones[j] -1
        gaps.append(gap)
        
    if gaps == []:
        return 0

    else:
        return max(gaps)


print(solution(1041))