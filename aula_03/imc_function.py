def calc_imc(peso,altura):
    calculo= peso / (altura*altura)

    if(calculo <= 17):
        return "Muito Baixo"
    elif( calculo >= 17 and calculo <18.49):
        return "Abaixo do Peso"
    elif( calculo >= 18.5 and calculo <24.99):
        return "Peso Normal"
    elif( calculo >= 25 and calculo < 29.99):
        return "Acima do Peso"
    elif( calculo >= 30.0 and calculo <34.99):
        return "Obesidade grau 1"
    elif( calculo >= 35 and calculo < 39.99):
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3(mórbida)"

resultado = calc_imc(110,1.90)
print(resultado)