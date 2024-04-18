
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from urllib.parse import parse_qs
from potionMediator import determineRecipe

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

    if "de" not in parameters:
        return PlainTextResponse(status_code = 400)
        
    rawDesiredEffects = parameters["de"]
    desiredEffects = []
    excludedIngredients = []

    if len(rawDesiredEffects) == 1:
        # Query string format: de=A,B,C
        desiredEffects = rawDesiredEffects[0].split(",")

    else:
        # Query string format: de=A&de=B&de=C
        desiredEffects = rawDesiredEffects

    if "ee" in parameters:
        rawExcludedIngredients = parameters["ee"]

        if len(rawExcludedIngredients) > 0:
            if len(rawDesiredEffects) == 1:
                # Query string format: de=A,B,C
                excludedIngredients = rawExcludedIngredients[0].split(",")

            else:
                # Query string format: de=A&de=B&de=C
                excludedIngredients = rawExcludedIngredients

    viablePotions = determineRecipe(desiredEffects, excludedIngredients)
    collectionResponse = createCollectionResponse(viablePotions)

    return JSONResponse(collectionResponse, 200)
