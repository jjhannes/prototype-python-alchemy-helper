
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import date

def getWeatherForecasts(request):
    weatherForecasts = [
        {
            "date": str(date.today()),
            "temperatureC": 24.6,
            "summary": "mild"
        }
    ]

    return JSONResponse(weatherForecasts, 200)

def configureWeatherForecastController(app: FastAPI):
    app.add_route("/pyapi/v1/weatherforecast", getWeatherForecasts, [ "GET" ])

    return app;
