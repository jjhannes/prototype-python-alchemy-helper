
from ingredientEffects import data

def isBadEffect(effect):
    effect = effect.lower()

    if "cure" in effect or "resist" in effect:
        return False
    
    return (
        "burden" in effect or
        "poison" in effect or
        "blind" in effect or
        "damage" in effect or
        "drain" in effect or
        "paralyz" in effect or
        "weakness" in effect or
        "vampirism" in effect
    )

def compileRecipe(ingredients, effects):
    return {
        "ingredients": ingredients,
        "effects": effects,
        "goodEffects": [effect for effect in effects if not isBadEffect(effect)],
        "badEffects": [effect for effect in effects if isBadEffect(effect)]
    }

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

def determineRecipe(desiredEffects, excludedIngredients = [], excludeBadPotions = False):
    if (excludedIngredients is None):
        excludedIngredients = []

    possibleRecipes = []
    ingredientsWithDesiredEffects = getIngredientsWithEffects(desiredEffects)

    if excludedIngredients is not None and len(excludedIngredients) > 0:
        countBeforeFilter = len(ingredientsWithDesiredEffects)

        ingredientsWithDesiredEffects = [iwde for iwde in ingredientsWithDesiredEffects if iwde not in excludedIngredients]

        if countBeforeFilter != len(ingredientsWithDesiredEffects):
            print(f"{countBeforeFilter - len(ingredientsWithDesiredEffects)} of {countBeforeFilter} excluded ingredients filtered out.")

    # Two ingredients
    for primary in range(len(ingredientsWithDesiredEffects)):
        primaryIngredient = ingredientsWithDesiredEffects[primary]

        for secondary in range(primary + 1, len(ingredientsWithDesiredEffects)):
            secondaryIngredient = ingredientsWithDesiredEffects[secondary]
            commonEffects = getCommonEffects([ primaryIngredient, secondaryIngredient ])

            if (all(item in commonEffects for item in desiredEffects)):
                possibleRecipes.append(compileRecipe([ primaryIngredient, secondaryIngredient ], commonEffects))

    # Three ingredients
    for primary in range(len(ingredientsWithDesiredEffects)):
        primaryIngredient = ingredientsWithDesiredEffects[primary]

        for secondary in range(primary + 1, len(ingredientsWithDesiredEffects)):
            secondaryIngredient = ingredientsWithDesiredEffects[secondary]
            
            for tertiary in range(secondary + 1, len(ingredientsWithDesiredEffects)):
                tertiaryIngredient = ingredientsWithDesiredEffects[tertiary]
                commonEffects = getCommonEffects([ primaryIngredient, secondaryIngredient, tertiaryIngredient ])

                if (all(item in commonEffects for item in desiredEffects)):
                    possibleRecipes.append(compileRecipe([ primaryIngredient, secondaryIngredient, tertiaryIngredient ], commonEffects))

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
                        # possibleRecipes.append([ primaryIngredient, secondaryIngredient, tertiaryIngredient, quaternaryIngredient ])
                        possibleRecipes.append(compileRecipe([ primaryIngredient, secondaryIngredient, tertiaryIngredient, quaternaryIngredient ], commonEffects))

    if excludeBadPotions:
        countBeforeFilter = len(possibleRecipes)

        possibleRecipes = [recipe for recipe in possibleRecipes if len(recipe["badEffects"]) < 1]

        if countBeforeFilter != len(possibleRecipes):
            print(f"{countBeforeFilter - len(possibleRecipes)} of {countBeforeFilter} recipies with bad effects filtered out.")

    return possibleRecipes
