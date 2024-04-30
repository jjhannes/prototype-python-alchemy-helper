
import pytest
from potionMediator import getRecipesWithDesiredEffects

@pytest.mark.parametrize("desiredEffects, expectedRecipeCount", [
    ([ "Swift Swim", "Water Breathing", "Restore Fatigue" ], 9),
    ([ "Fortify Speed", "Water Walking" ], 168),
    ([ "Restore Health" ], 246),
    ([ "Restore Health", "Fortify Health" ], 216),
    ([ "Restore Magicka" ], 91),
    ([ "Restore Magicka", "Fortify Magicka" ], 126),
    ([ "Cure Common Disease", "Cure Poison" ], 588),
    ([ "Cure Blight Disease", "Cure Poison" ], 71),
    ([ "Cure Blight Disease", "Cure Common Disease" ], 63)
])
def test_desiredEffectsGivesXRecipesWithAtLeastAllDesiredEffects(desiredEffects, expectedRecipeCount):
    actualRecipes = getRecipesWithDesiredEffects(desiredEffects)

    assert len(actualRecipes) == expectedRecipeCount

    for recipe in actualRecipes:
        assert set(desiredEffects).issubset(recipe["goodEffects"]) == True

@pytest.mark.parametrize("desiredEffects, excludedIngredients, expectedRecipeCount", [
    ([ "Swift Swim", "Water Breathing", "Restore Fatigue" ], [  ], 9),
    ([ "Fortify Speed", "Water Walking" ], [ "Meadow Rye", "Nirthfly Stalks" ], 90),
    ([ "Restore Health" ], [ "Emerald", "Raw Stalhrim", "Sweetpulp" ], 50),
    ([ "Restore Health", "Fortify Health" ], [ "Emerald", "Raw Stalhrim", "Sweetpulp" ], 90),
    ([ "Restore Magicka" ], [ "Adamantium Ore", "Heartwood", "Frost Salts", "Void Salts" ], 4),
    ([ "Restore Magicka", "Fortify Magicka" ], [ "Adamantium Ore", "Heartwood", "Frost Salts", "Void Salts" ], 18)
])
def test_desiredEffectsExcludingIngredientsGivesXRecipesWithAtLeastAllDesiredEffects(desiredEffects, excludedIngredients, expectedRecipeCount):
    actualRecipes = getRecipesWithDesiredEffects(desiredEffects, excludedIngredients)

    assert len(actualRecipes) == expectedRecipeCount

    for recipe in actualRecipes:
        assert set(desiredEffects).issubset(recipe["goodEffects"]) == True

@pytest.mark.parametrize("desiredEffects, excludedIngredients, expectedGoodRecipeCount", [
     ([ "Swift Swim", "Water Breathing", "Restore Fatigue" ], [ "Daedra Skin", "Golden Sedge Flowers", "Pearl" ], 2),
     ([ "Fortify Speed", "Water Walking" ], [ "Meadow Rye", "Nirthfly Stalks", "Moon Sugar", "Snow Bear Pelt", "Snow Wolf Pelt", "Wolf Pelt" ], 0),
     ([ "Restore Health", "Fortify Health" ], [ "Human Flesh", "Corprus Weepings", "Vampire Dust", "Emerald", "Raw Stalhrim", "Sweetpulp" ], 3),
     ([ "Restore Magicka", "Fortify Magicka" ], [ "Adamantium Ore", "Heartwood", "Frost Salts", "Void Salts", "Emerald" ], 9)
])
def test_desiredEffectsExcludingIngredientsGivesXGoodOnlyRecipesWithAtLeastAllDesiredEffects(desiredEffects, excludedIngredients, expectedGoodRecipeCount):
    actualRecipes = getRecipesWithDesiredEffects(desiredEffects, excludedIngredients, True)

    assert len(actualRecipes) == expectedGoodRecipeCount

    for recipe in actualRecipes:
        assert set(desiredEffects).issubset(recipe["goodEffects"]) == True
        assert len(recipe["badEffects"]) == 0

@pytest.mark.parametrize("desiredEffects, expectedRecipeCount", [
    ([ "Swift Swim", "Water Breathing", "Restore Fatigue" ], 5),
    ([ "Fortify Speed", "Water Walking" ], 22),
    ([ "Restore Health", "Fortify Health" ], 66),
    ([ "Restore Magicka", "Fortify Magicka" ], 66)
])
def test_desiredEffectsMatchedExactly(desiredEffects, expectedRecipeCount):
    actualRecipes = getRecipesWithDesiredEffects(desiredEffects, exactlyMatchDesiredEffects = True)

    assert len(actualRecipes) == expectedRecipeCount

    for recipe in actualRecipes:
        assert sorted(recipe["goodEffects"]) == sorted(desiredEffects)
