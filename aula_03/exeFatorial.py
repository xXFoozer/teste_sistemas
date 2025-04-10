def fatorial(num: int)-> int:
    if num < 0:
        raise ValueError("não pode ser negativo")
    result = 1

    for i in range(2,num + 1):
        result *= i
    return result