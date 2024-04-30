
import pytest
from potionMediator import validateEffects, validateIngredients

@pytest.mark.parametrize("givenIngredients, expectedInvalidIngredients", [
    ([ "Gravedust" ], []),
    ([ "racer plumes" ], []),
    ([ "Kaas" ], [ "Kaas" ])
])
def test_ingredientsValidation(givenIngredients, expectedInvalidIngredients):
    actual = validateIngredients(givenIngredients)

    assert sorted(expectedInvalidIngredients) == sorted(actual)

@pytest.mark.parametrize("givenEffects, expectedInvalidEffects", [
    ([ "Restore Health" ], []),
    ([ "restore fatigue" ], []),
    ([ "Super Strength" ], [ "Super Strength" ])
])
def test_effectsValidation(givenEffects, expectedInvalidEffects):
    actual = validateEffects(givenEffects)

    assert len(expectedInvalidEffects) == len(actual)
    assert sorted(expectedInvalidEffects) == sorted(actual)
