
from potionMediator import *
from potionMediator import determineRecipe

def promptDesiredEffectsAndCalculateRecipe():
    promptDescription()

    desiredEffects = []
    done = False
    effect = None
    
    while (not done):
        effect = input("")

        if (effect == ""):
            if (len(desiredEffects) < 1):
                promptEmptyInput()

                continue

            else:
                done = True

                continue
        else:
            desiredEffects.append(effect)

    possibleRecipes = determineRecipe(desiredEffects)

    if (len(possibleRecipes) < 1):
        print(f"There are no recipes that will grant [{" & ".join(desiredEffects)}]")

    else:
        print(f"There are {len(possibleRecipes)} recipes that will grant [{" & ".join(desiredEffects)}]:")
        print("")

        for recipe in possibleRecipes:
            print(recipe)
            print("")

def promptDescription():
    print("What effects would you like your potion to have?")
    print("(Press <Enter> to submit and provide additional desired effects)")
    print("(Press <Enter> again, i.e. empty value, to accept your selection)")

def promptEmptyInput():
    print("")
    print("You've not provided any desired effects. Please provide a desired effect.")

def main():
    promptDesiredEffectsAndCalculateRecipe()

if __name__ == "__main__":
    main()
