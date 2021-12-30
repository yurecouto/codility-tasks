def solution(N):
    binary = bin(N).replace('0b', '')
    ones = []
    gaps = []

    for i in range(len(binary)):            # this for loop separates the number ones by theis positions                             
        if binary[i] == '1':                # then I'm able to see the the size of the gap
            ones.append(i)

    for j in range(len(ones) - 1):          # Now the idea is to invert the list, so i could subtract two of them
        gap = ones[j+1] - (ones[j] + 1)     # returning the number of zeros (the gap) between two ones

        gaps.append(gap)
        
    print(binary)
    print(ones)
    print(gaps)

    if gaps == []:
        return 0

    else:
        return max(gaps)
        

solution(1041)