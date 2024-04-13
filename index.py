
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

def getEffectsForIngredient(ingredient):
    return data[ingredient]

def getIngredientsWithEffects(effects):
    ingredients = []

    for ingredient in data:
        ingredientEffects = data[ingredient]

        if any(check in ingredientEffects for check in effects):
            ingredients.append(ingredient)      

    return ingredients

def main():
    runTests()

if __name__ == "__main__":
    main()
