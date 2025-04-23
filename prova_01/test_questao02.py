import pytest
from questao02 import  questao02 

@pytest.mark.parametrize("matricula,salario,tempoEmpresa,esperado",[
    (123,1500.01,3,"Junior"),
    (456,5000.50,7,"Sênior"),
    (789,30000.00,15,"Pleno")
])

def test_questao02(matricula,salario,tempoEmpresa,esperado):
    assert questao02(matricula,salario,tempoEmpresa) == esperado