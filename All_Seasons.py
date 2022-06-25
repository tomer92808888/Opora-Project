# Importing the essential libraries
import pandas as pd

# Importing the essential classes
from Data import Data
from Season import Season


# Getting the preprocessed data
data = Data('csv')
data.get_csv_names()
DATA = data.clean()

class All_Seasons():
    def __init__(self):
        """
        Initializes the class with a list of all the season years
        """
        self.SEASONS = [Season(i) for i in DATA['seasons']['year']]

    def get_seasons(self) -> list:
        """
        Returns a list of all the season years
        """
        return self.SEASONS

    def top_3_each_season(self) -> pd.DataFrame:
        """
        Returns a dataframe of the top 3 drivers in each season
        """
        top_3_each_season = pd.DataFrame()
        for i in self.get_seasons():
            top_3_each_season = top_3_each_season.append(i.get_top_3())
        return top_3_each_season.sort_values(by='Season')