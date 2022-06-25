# Importing the essential libraries
from fastapi import HTTPException
import pandas as pd

# Importing the essential classes
from Data import Data
from Race_Wins import Race_Wins
from Driver import Driver

# Getting the preprocessed data
data = Data('csv')
data.get_csv_names()
DATA = data.clean()

class Season():
    def __init__(self, year):
        """
        Initializes the class with the given season and checks if the input is a string if not it raises an error and if the season exists in the dataset
        """
        if type(year) == int:
            self.YEAR = year
            if year >= 1950 and year <= 2021:
                self.RACES = [Race_Wins(i) for i in DATA['races'][DATA['races']['year'] == self.YEAR]['raceId']]
            else:
                raise HTTPException(status_code=404 ,detail="The season isn't in the dataset")
        else:
            raise HTTPException(status_code=404 ,detail="Season must be an int")
    
    def get_year(self) -> int:
        """
        Returns the season year
        """
        return self.YEAR

    def get_races(self):
        """
        Returns a list of the Race_Wins class from the given season
        """
        return self.RACES

    def get_drivers(self) -> pd.DataFrame:
        """
        Returns a dataframe of all the drivers from the given season and adding their position in the season
        """
        drivers = self.get_races()[0].results()
        for i in self.get_races():
            if i != 0:
                drivers = pd.merge(drivers,i.results(),on='driverId')
                drivers['position'] = drivers["position_x"].astype(int) + drivers["position_y"].astype(int)
                drivers = drivers.drop(['position_x', 'position_y'], axis=1) # Removing the old columns so it will be easier to merge with the other dataframes
        return drivers

    def get_sorted_by_wins(self) -> pd.DataFrame:
        """
        Returns a dataframe of all the drivers in the season in order of the number of wins
        """
        drivers = self.get_drivers()
        drivers = drivers.sort_values(by='position')
        drivers = drivers.drop('position', axis=1).reset_index(drop=True)
        
        drivers_df = pd.DataFrame()
        for id in drivers['driverId']:
            drivers_df = drivers_df.append(Driver(id).get_info())
            drivers_df["Season"] = self.get_year()
        return drivers_df
    

    def get_top_3(self) -> pd.DataFrame:
        """
        Returns a dataframe of the top 3 drivers in the season
        """
        return self.get_sorted_by_wins().head(3)