
from ingredientEffects import data

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

def getEffectsForIngredient(ingredient):
    return data[ingredient]

def getIngredientsWithEffects(effects):
    ingredients = set()

    for ingredient in data:
        ingredientEffects = data[ingredient]

        if any(check in ingredientEffects for check in effects):
            ingredients.update([ ingredient ])      

    return list(ingredients)

def getCommonEffects(ingredients):
    commonEffects = set()

    for primary in range(len(ingredients)):
        primaryIngredient = ingredients[primary]
        primaryIngredientEffects = getEffectsForIngredient(primaryIngredient)

        for secondary in range(primary + 1, len(ingredients)):
            secondaryIngredient = ingredients[secondary]
            secondaryIngredientEffects = getEffectsForIngredient(secondaryIngredient)

            commonEffects.update(list(set(primaryIngredientEffects).intersection(secondaryIngredientEffects)))

            # Alternative approach
            # commonEffects.update([element for element in primaryIngredientEffects if element in secondaryIngredientEffects])

    return list(commonEffects)

def determineRecipe(desiredEffects):
    possibleRecipes = []
    ingredientsWithDesiredEffects = getIngredientsWithEffects(desiredEffects)

    # Two ingredients
    for primary in range(len(ingredientsWithDesiredEffects)):
        primaryIngredient = ingredientsWithDesiredEffects[primary]

        for secondary in range(primary + 1, len(ingredientsWithDesiredEffects)):
            secondaryIngredient = ingredientsWithDesiredEffects[secondary]
            commonEffects = getCommonEffects([ primaryIngredient, secondaryIngredient ])

            if (all(item in commonEffects for item in desiredEffects)):
                possibleRecipes.append([ primaryIngredient, secondaryIngredient ])

    # Three ingredients
    for primary in range(len(ingredientsWithDesiredEffects)):
        primaryIngredient = ingredientsWithDesiredEffects[primary]

        for secondary in range(primary + 1, len(ingredientsWithDesiredEffects)):
            secondaryIngredient = ingredientsWithDesiredEffects[secondary]
            
            for tertiary in range(secondary + 1, len(ingredientsWithDesiredEffects)):
                tertiaryIngredient = ingredientsWithDesiredEffects[tertiary]
                commonEffects = getCommonEffects([ primaryIngredient, secondaryIngredient, tertiaryIngredient ])

                if (all(item in commonEffects for item in desiredEffects)):
                    possibleRecipes.append([ primaryIngredient, secondaryIngredient, tertiaryIngredient ])

    # Four ingredients
    for primary in range(len(ingredientsWithDesiredEffects)):
        primaryIngredient = ingredientsWithDesiredEffects[primary]

        for secondary in range(primary + 1, len(ingredientsWithDesiredEffects)):
            secondaryIngredient = ingredientsWithDesiredEffects[secondary]
            
            for tertiary in range(secondary + 1, len(ingredientsWithDesiredEffects)):
                tertiaryIngredient = ingredientsWithDesiredEffects[tertiary]
                
                for quaternary in range(tertiary + 1, len(ingredientsWithDesiredEffects)):
                    quaternaryIngredient = ingredientsWithDesiredEffects[quaternary]
                    commonEffects = getCommonEffects([ primaryIngredient, secondaryIngredient, tertiaryIngredient, quaternaryIngredient ])

                    if (all(item in commonEffects for item in desiredEffects)):
                        possibleRecipes.append([ primaryIngredient, secondaryIngredient, tertiaryIngredient, quaternaryIngredient ])

    return possibleRecipes

def main():
    runTests()

if __name__ == "__main__":
    main()
