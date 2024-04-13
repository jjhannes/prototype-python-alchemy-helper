
from ingredientEffects import data;

def runTests():
    # Test get effects for ingredient
    ingredients = getEffectsForIngredient("Kagouti Hide");

    print(ingredients);

def getEffectsForIngredient(ingredient):
    return data[ingredient];

def main():
    runTests();

if __name__ == "__main__":
    main();
