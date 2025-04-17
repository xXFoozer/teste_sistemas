
def Cadastro (nome, telefone, email, idade):
   if " " in nome and "48" in telefone and "@" in email and ".":
    return True
   else:
    return "dados invalidos"

