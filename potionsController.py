
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from urllib.parse import parse_qs
from potionMediator import determineRecipe

def determineRecipesWithDesiredEffects(request):
    parameters = parse_qs(str(request.query_params))
    rawDesiredEffects = parameters["de"]
    desiredEffects = []

    if (len(rawDesiredEffects) == 1):
        # Query string format: de=A,B,C
        desiredEffects = rawDesiredEffects[0].split(",")

    else:
        # Query string format: de=A&de=B&de=C
        desiredEffects = rawDesiredEffects

    viablePotions = determineRecipe(desiredEffects)

    return JSONResponse(viablePotions, 200)

def configurePotionsController(app: FastAPI):
    app.add_route("/pyapi/v1/potions/recipes/with-effects", determineRecipesWithDesiredEffects, [ "GET" ])

    return app;
