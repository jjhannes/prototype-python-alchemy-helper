
import pytest
from potionMediator import getRecipeFromIngedients

@pytest.mark.parametrize("givenIngredients, expectedEffects", [
    ([ "Bread", "Hound Meat" ], [ "Restore Fatigue" ]),
    ([ "Corprus Weepings", "Small Corprusmeat Hunk" ], [ "Drain Fatigue" ]),
    ([ "Bread", "Corprus Weepings" ], [  ]),
    ([ "corkbulb root", "large kwama egg", "resin", "shalk resin" ], [ "Fortify Health", "Restore Health" ])
])
def test_getRecipeFromIngredients(givenIngredients,expectedEffects):
    # givenIngredients = [ "Bread", "Hound Meat" ]
    # expectedEffects = [ "Restore Fatigue" ]
    resultingRecipe = getRecipeFromIngedients(givenIngredients)

    assert len(expectedEffects) == len(resultingRecipe["effects"])
    assert sorted(expectedEffects) == sorted(resultingRecipe["effects"])
