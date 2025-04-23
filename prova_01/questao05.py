def classifica_idade(idade):
    if idade < 16:
        return "Não pode votar"
    elif (idade == 16) or (idade <= 17):
        return "Pode votar"
    elif (idade == 18) or (idade <=34):
        return "Deve votar, mas não pode ser presidente"
    elif (idade >34) and (idade <71):
        return "Deve votar e pode ser presidente"
    else:
        return "Pode votar e pode ser presidente"