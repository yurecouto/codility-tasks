# the hole code is about to verify if the built in function round makes the number bigger of smaller than it needs to be

def solution(X, Y, D):
    difference = (Y - X)
    float_s = difference / D            
    round_s = round(difference / D)
    
    if float_s > round_s:
        solution = round_s + 1
        return solution
    
    elif float_s < round_s:
        return round_s

    elif float_s == round_s:
        return round_s

print(solution(10, 85, 30))