def calculadora(value1,value2,operador):
    if operador == "+":
        return value1 + value2
    elif operador == "-":
        return value1 - value2
    elif operador == "*":
        return value1 * value2
    elif operador == "/":
        return value1 / value2
    else:
        return "Operador invalido"