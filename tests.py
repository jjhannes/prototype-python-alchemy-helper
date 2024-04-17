
from potionMediator import *

def runTests():
    # Test get effects for ingredient
    kagoutiHide = "Kagouti Hide"
    ingredients = getEffectsForIngredient(kagoutiHide)

    print(f"{kagoutiHide} gives {ingredients}")

    # Test get ingredients with effects
    waterBreathing = [ "Water Breathing" ]
    waterBreathingIngredients = getIngredientsWithEffects(waterBreathing)

    print(f"{waterBreathing} comes from {waterBreathingIngredients}")

    # Test get common effects
    scalesAndKwamaCuttle = [ "Scales", "Kwama Cuttle" ]
    commonEffects = getCommonEffects(scalesAndKwamaCuttle)

    print(f"[{" & ".join(scalesAndKwamaCuttle)}] has [{" & ".join(commonEffects)}] in common")

    # Test determine recipe
    desiredEffects = [ "Water Walking", "Fortify Speed" ]
    possibleRecipes = determineRecipe(desiredEffects)

    print(f"There are {len(possibleRecipes)} recipes that will give you [{" & ".join(desiredEffects)}]:")
    [print(f" - {recipe}") for recipe in possibleRecipes]
