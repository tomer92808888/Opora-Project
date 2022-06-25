# Importing the essential libraries
import pandas as pd

# Importing the essential classes
from Data import Data
from Personal_Race import Personal_Race

# Getting the preprocessed data
data = Data('csv')
data.get_csv_names()
DATA = data.clean()


def is_int(element) -> bool:
    """
    Checks if the element can be converted into int
    """
    try:
        int(element)
        return True
    except ValueError:
        return False

class Driver():
    def __init__(self, driver_id_or_name):
        """
        Initializes the class with the corresponding driver's ID or driver's name
        """
        # Checks if the value can be converted into int
        if is_int(driver_id_or_name):
            driver_id_or_name = int(driver_id_or_name)
            self.ID = driver_id_or_name
        # Checks if the value is a string
        elif type(driver_id_or_name) == str:
            # Splitting the string into forename and surname to get the driver's ID
            name = driver_id_or_name.split(" ")
            forename = name[0]
            surname = " ".join(name[1:])
            self.ID = DATA['drivers'][(DATA['drivers']['forename'] == forename) & (DATA['drivers']['surname'] == surname)]['driverId'].values[0]
        else:
            # If the value is not a string or int, raise an error
            raise TypeError("Driver's ID must be an int or Driver's name must be a string")

    def get_ID(self) -> int:
        """
        Returns the Driver's ID
        """
        return self.ID

    def get_info(self) -> pd.DataFrame:
        """
        Returns the full row of the driver's information from drivers.csv
        """
        return DATA['drivers'][DATA['drivers']['driverId'] == self.get_ID()]

    def get_races(self) -> pd.DataFrame:
        """
        Returns all the race IDs that the driver's took a part of 
        """
        return DATA['results'][DATA['results']['driverId'] == self.get_ID()]['raceId']

    def driver_profile(self) -> pd.DataFrame:
        """
        Gets the driver's profile from a list of all of his Personal_Race dataframes and contacting them into one dataframe before sorting them according to the season
        """
        Races_dfs =  [Personal_Race(self.get_ID(),i).get_dataframe() for i in self.get_races()]
        df = pd.DataFrame()
        for i in Races_dfs:
            df = pd.concat([df, i])
        return df.sort_values('Season')