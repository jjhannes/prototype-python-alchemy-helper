
import sys
from fastapi import FastAPI
import uvicorn
from weatherForecastsController import configureWeatherForecastController
from potionsController import configurePotionsController

def createApp():
    port = 6668

    app = FastAPI()

    configureWeatherForecastController(app)
    configurePotionsController(app)

    return app, port

if __name__ == "__main__":
    app, port = createApp()

    uvicorn.run(app, port = port)
    
    # TODO: Proper uvicorn implementation and usage(https://www.uvicorn.org/#the-asgi-interface)
    # ucConfig = uvicorn.Config("index:app", port = port, log_level = "info")
    # ucServer = uvicorn.Server(ucConfig)
    # ucServer.run()

    

