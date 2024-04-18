
from fastapi import FastAPI
import uvicorn
from weatherForecastsController import configureWeatherForecastController
from potionsController import configurePotionsController

port = 6668

app = FastAPI()

configureWeatherForecastController(app)
configurePotionsController(app)

if __name__ == "__main__":
    uvicorn.run(app, port=port)

