
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from urllib.parse import parse_qs
from potionMediator import determineRecipe

parameterNames = {
    "desiredEffects": "de",
    "excludedIngredients": "ei",
    "excludeBadPotions": "ebp",
    "exactlyMatchDesiredEffects": "emde"
}

def configurePotionsController(app: FastAPI):
    app.add_route("/pyapi/v1/potions/recipes/with-effects", determineRecipesWithDesiredEffects, [ "GET" ])

    return app;

def createCollectionResponse(collection):
    return {
        "count": len(collection),
        "items": collection
    }

def determineRecipesWithDesiredEffects(request):
    parameters = parse_qs(str(request.query_params))

    if parameterNames["desiredEffects"] not in parameters:
        return PlainTextResponse(status_code = 400)
        
    rawDesiredEffects = parameters[parameterNames["desiredEffects"]]
    desiredEffects = []
    excludedIngredients = []
    excludeBadPotions = False
    exactlyMatchDesiredEffects = False

    if len(rawDesiredEffects) == 1:
        # Query string format: de=A,B,C
        desiredEffects = rawDesiredEffects[0].split(",")

    else:
        # Query string format: de=A&de=B&de=C
        desiredEffects = rawDesiredEffects

    if parameterNames["excludedIngredients"] in parameters:
        rawExcludedIngredients = parameters[parameterNames["excludedIngredients"]]

        if len(rawExcludedIngredients) > 0:
            if len(rawDesiredEffects) == 1:
                # Query string format: de=A,B,C
                excludedIngredients = rawExcludedIngredients[0].split(",")

            else:
                # Query string format: de=A&de=B&de=C
                excludedIngredients = rawExcludedIngredients

    if parameterNames["excludeBadPotions"] in parameters:
        rawExcludeBadPotions = parameters[parameterNames["excludeBadPotions"]]

        if len(rawExcludeBadPotions) > 0:
            rawExcludeBadPotions = rawExcludeBadPotions[0]

        excludeBadPotions = (
            rawExcludeBadPotions.lower() == "true" or
            rawExcludeBadPotions.lower() == "1"
        )

    if parameterNames["exactlyMatchDesiredEffects"] in parameters:
        rawExactlyMatchDesiredEffects = parameters[parameterNames["exactlyMatchDesiredEffects"]]

        if len(rawExactlyMatchDesiredEffects) > 0:
            rawExactlyMatchDesiredEffects = rawExactlyMatchDesiredEffects[0]
    
        exactlyMatchDesiredEffects = (
            rawExactlyMatchDesiredEffects.lower() == "true" or
            rawExactlyMatchDesiredEffects.lower() == "1"
        )

    viablePotions = determineRecipe(desiredEffects, excludedIngredients, excludeBadPotions, exactlyMatchDesiredEffects)
    collectionResponse = createCollectionResponse(viablePotions)

    return JSONResponse(collectionResponse, 200)
