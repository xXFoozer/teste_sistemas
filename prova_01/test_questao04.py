import pytest
from questao01 import calculadora


@pytest.mark.parametrize("value1,operador,value2,esperado",[
    (1,'+',2,3),
    (2,'-',1,1),
    (1,'*',2,2),
    (1,'/',2,0.5),
    (5,'+',5,10),
    (15,'-',5,10),
    (40,'-',20,20),
    (15,'/',5,3),
    (1,'+',1,2),
    (4,'*',2,8),
    (4,'*',1,4),
    (5,'*',1,5),
    (5,'*',2,10),
    (5,'*',9,45),
    (5,'*',10,50),
    (8,'+',8,16),
    (16,'+',1,17),
    (2,'*',9,18),
    (20,'-',1,19),
    (20,'*',1,20),
])

def test_calculadora(value1,value2,operador,esperado):
    assert calculadora(value1,value2,operador) == esperado