def usuario(nome,email,idade,telefone):
    if " " in nome and "48" in telefone and "@" in email:
        return{
            "nome":nome,
            "telefone":telefone,
            "email":email,
            "idade":idade
        }
    else:
        return "Dados invalidos: verifique nome,telefone ou email"
    


def salario(salario,comissao,inss):
    s3 = salario + (salario * comissao),
    s4 = (salario * inss)
    total = s3 - s4
    return round(total,2)