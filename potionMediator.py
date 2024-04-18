
from ingredientEffects import data


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

def determineRecipe(desiredEffects, excludedIngredients = []):
    if (excludedIngredients is None):
        excludedIngredients = []

    possibleRecipes = []
    ingredientsWithDesiredEffects = getIngredientsWithEffects(desiredEffects)

    if (excludedIngredients is not None and len(excludedIngredients) > 0):
        ingredientsWithDesiredEffects = [iwde for iwde in ingredientsWithDesiredEffects if iwde not in excludedIngredients]

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
