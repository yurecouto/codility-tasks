def solution(X, Y, D):
    difference = (Y - X)                # A diferença é a distancia que falta para que o sapo atravesse
    float_s = difference / D            # Essa diferença é um numero flutuante muitas das vezes
    round_s = round(difference / D)     # esta variável retorna um numero arredondado
    
    if float_s > round_s:
        solution = round_s + 1
        return solution
    
    elif float_s < round_s:
        return round_s

    elif float_s == round_s:
        return round_s

print(solution(10, 85, 30))