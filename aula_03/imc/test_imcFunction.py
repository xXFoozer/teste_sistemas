import pytest
from peso_altura import peso_altura

@pytest.mark.parametrize("peso , altura, esperando",[
    (10,1.75,'Muito abaixo do peso ideal')
])

def test_imc(peso,altura,esperando):
    assert peso_altura(peso,altura) == esperando
