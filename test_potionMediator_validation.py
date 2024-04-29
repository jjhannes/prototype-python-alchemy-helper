
from potionMediator import *

def test_validEffects():
    input = [ "Restore Health" ]
    expected = []
    actual = validateEffects(input)

    assert sorted(expected) == sorted(actual)

def test_validEffect_caseInsensitive():
    input = [ "restore fatigue" ]
    expected = []
    actual = validateEffects(input)

    assert sorted(expected) == sorted(actual)

def test_invalidEffect():
    input = [ "Super Strength" ]
    expected = input.copy()
    actual = validateEffects(input)

    assert sorted(expected) == sorted(actual)

def test_validIngredient():
    input = [ "Gravedust" ]
    expected = []
    actual = validateIngredients(input)

    assert sorted(expected) == sorted(actual)

def test_validIngredient_caseInsensitive():
    input = [ "racer plumes" ]
    expected = []
    actual = validateIngredients(input)

    assert sorted(expected) == sorted(actual)

def test_invalidIngredient():
    input = [ "Kaas" ]
    expected = input.copy()
    actual = validateIngredients(input)

    assert sorted(expected) == sorted(actual)
