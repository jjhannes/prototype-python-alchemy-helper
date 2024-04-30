
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

def isIngredient(ingredient: str):
    return ingredient.lower() in [key.lower() for key in data.keys()]

def isEffect(effect: str):
    return effect.lower() in set([x.lower() for xs in data.values() for x in xs])

def compileRecipe(ingredients, effects):
    return {
        "ingredients": sorted(ingredients),
        "effects": sorted(effects),
        "goodEffects": sorted([effect for effect in effects if not isBadEffect(effect)]),
        "badEffects": sorted([effect for effect in effects if isBadEffect(effect)])
    }

def getEffectsForIngredient(ingredient:str) -> list[str]:
    sourceIngredientKey = [key for key in data.keys() if key.lower() == ingredient.lower()][0]
    
    return data[sourceIngredientKey]

def getIngredientsWithEffects(effects):
    ingredients = set()

    for ingredient in data:
        # ingredientEffects = data[ingredient]
        ingredientEffects = getEffectsForIngredient(ingredient)

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

# Validates the given ingredients and returns a list of invalid ingredients.
# That means, if the returned collection is empty, all the given ingredients are valid.
# Conversely, if the list contains any elements, those ingredients are considered invalid.
def validateIngredients(ingredients):
    return [ingredient for ingredient in ingredients if not isIngredient(ingredient)]

# Validates the given effects and returns a list of invalid effects.
# That means, if the returned collection is empty, all the given effects are valid.
# Conversely, if the list contains any elements, those effects are considered invalid.
def validateEffects(effects):
    return [effect for effect in effects if not isEffect(effect)]

def getRecipesWithDesiredEffects(desiredEffects, excludedIngredients = [], excludeBadPotions = False, exactlyMatchDesiredEffects = False):
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

    if exactlyMatchDesiredEffects:
        countBeforeFilter = len(possibleRecipes)

        possibleRecipes = [recipe for recipe in possibleRecipes if set(recipe["effects"]) == set(desiredEffects)]

        if countBeforeFilter != len(possibleRecipes):
            print(f"{countBeforeFilter - len(possibleRecipes)} of {countBeforeFilter} recipies with additional good effects filtered out.")

    possibleRecipes = sorted(possibleRecipes, key = lambda recipe: (len(recipe["badEffects"]), len(recipe["ingredients"]), -len(recipe["goodEffects"])), reverse = False)

    return possibleRecipes

def getRecipeFromIngedients(ingredients):
    effects = getCommonEffects(ingredients)
    sourceIngredients = [ingredient for ingredient in data.keys() if ingredient.lower() in ingredients]
    compiledRecipe = compileRecipe(sourceIngredients, effects)

    return compiledRecipe
