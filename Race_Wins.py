# Importing the essential classes
from Data import Data
import pandas as pd

# Getting the preprocessed data
data = Data('csv')
data.get_csv_names()
DATA = data.clean()

class Race_Wins():
    def __init__(self, race_id):
        """
        Initializes the class with the given Race's ID and create a dataframe with the results of the race
        """
        self.RACE_ID = race_id
        self.RACE_DATASET = DATA['results'][DATA['results']['raceId'] == self.RACE_ID]

    def get_race_dataset(self) -> pd.DataFrame:
        """
        Returns the race's result dataframe
        """
        return self.RACE_DATASET

    def results(self) -> pd.DataFrame:
        """
        Returns the driver IDs and their position in the current race
        """
        return self.get_race_dataset()[['driverId', 'position']]