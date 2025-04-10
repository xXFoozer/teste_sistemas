def peso_altura(peso, altura):
    imc = peso / (altura * altura)
    if imc < 17:
        return "Muito abaixo do peso ideal"
    elif imc >= 17 and imc <= 18.49:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.99:
        return "Peso normal"
    elif imc >= 25 and imc <= 29.99:
        return "Acima do Peso"
    elif imc >= 30 and imc <= 34.99:
        return "Obesidade grau 1"
    elif imc >= 35 and imc <= 39.99:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3 (mórbida)"