import pytest
from exeFatorial import fatorial

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_um():
    assert fatorial(1) == 1

def test_fatorial_positivo():
    assert fatorial(5) == 120