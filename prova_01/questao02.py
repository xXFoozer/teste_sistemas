def questao02(matricula,salario,tempoEmpresa):
    if not((matricula == "@") or (matricula =="$") or (matricula == "#") or (matricula == "-") or (matricula == "_")):
        if (salario < 4000.00) or (tempoEmpresa < 5):
            return "Junior"
        elif (salario >= 4000.01 and salario < 10000.00) or (tempoEmpresa >= 6 and tempoEmpresa < 10):
            return "Sênior"
        else:
            return "Pleno"
    else:
        return "Funcionario não é VALIDO"