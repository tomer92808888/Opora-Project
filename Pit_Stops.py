# Importing the essential libraries
import pandas as pd

class Pit_Stops():
    def __init__(self, pits):
        """
        Initializes the class with given pits and if there are no pits it will create a new dataframes with 0 as values to make sure that the calculations will work
        """
        if pits.empty:
            self.PITS = pd.DataFrame({'stop': [0],'milliseconds': [0]})
        else:
            self.PITS = pits
    
    def get_pits(self) -> pd.DataFrame:
        return self.PITS

    def milliseconds_to_time(self, milliseconds) -> str:
        """
        Converts the given milliseconds to a time format
        """
        minutes= int((milliseconds/(1000*60))%60)
        seconds= int((milliseconds/1000)%60)
        milliseconds = int(milliseconds%1000)
        return str(minutes) + ':' + str(seconds) + '.' + str(milliseconds)

    def number_of_pit_stops(self) -> int:
        """
        Returns the number of pit stops
        """
        return self.get_pits().shape[0]

    def get_fastest_pit_stop(self):
        """
        Returns the fastest pit stop time and the stop it was on
        """
        fastest_milliseconds = self.get_pits()['milliseconds'].min()
        fastest_pit = self.get_pits()[self.get_pits()['milliseconds'] == fastest_milliseconds]['stop'].values[0]
        return self.milliseconds_to_time(fastest_milliseconds), int(fastest_pit)

    def get_slowest_pit_stop(self):
        """
        Returns the slowest pit stop time and the stop it was on
        """
        slowest_milliseconds = (self.get_pits()['milliseconds'].max())
        slowest_pit = self.get_pits()[self.get_pits()['milliseconds'] == slowest_milliseconds]['stop'].values[0]
        return self.milliseconds_to_time(slowest_milliseconds), int(slowest_pit)