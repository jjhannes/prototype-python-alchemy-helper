
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

def getEffectsForIngredient(ingredient):
    return data[ingredient]

def getIngredientsWithEffects(effects):
    ingredients = []

    for ingredient in data:
        ingredientEffects = data[ingredient]

        if any(check in ingredientEffects for check in effects):
            ingredients.append(ingredient)      

    return ingredients

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

def main():
    runTests()

if __name__ == "__main__":
    main()
