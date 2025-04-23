import pytest
from questao05 import classifica_idade


@pytest.mark.parametrize("idade,categoria_esperada",[
    (10,"Não pode votar"),
    (16,"Pode votar"),
    (24,"Deve votar, mas não pode ser presidente"),
    (70,"Deve votar e pode ser presidente"),
    (81,"Pode votar e pode ser presidente")
    ])


def test_classifica_idade(idade,categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada