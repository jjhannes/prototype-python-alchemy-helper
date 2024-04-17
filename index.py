
from fastapi import FastAPI
import uvicorn
from weatherForecastsController import configureWeatherForecastController

# TODO: Create API
app = FastAPI()

configureWeatherForecastController(app)

if __name__ == "__main__":
    uvicorn.run(app, port=6668)
