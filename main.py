# Importing the essential libraries
from fastapi import FastAPI
import json


# Importing the essential classes
from API_Functions import API_Functions

# Creating the API and getting the API's function
app = FastAPI()
functions = API_Functions()

# Creating the index endpoint
@app.get("/")
def root():
    return {"message": "Go to docs to see the API documentation"}

# Creating the drivers_by_season endpoint
@app.get("/drivers_by_season/{season}")
def read_root(season: int) -> json:
    return functions.drivers_by_season(season)

# Creating the seasons_all_time_ranking endpoint
@app.get("/seasons_all_time_ranking/{season}")
def read_root(season: int) -> json:
    return functions.seasons_all_time_ranking(season)

# Creating the driver_profile endpoint
@app.get("/driver_profile/{driver_id_or_name}")
def read_root(driver_id_or_name: str) -> json:
    return functions.driver_profile(driver_id_or_name)
