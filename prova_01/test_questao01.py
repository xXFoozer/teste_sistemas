import pytest
from questao01 import calculadora

@pytest.mark.parametrize("value1,operador,value2,esperado",[
    (1,'+',2,3),
    (2,'-',1,1),
    (1,'*',2,2),
    (1,'/',2,0.5)
])

def test_calculadora(value1,value2,operador,esperado):
    assert calculadora(value1,value2,operador) == esperado