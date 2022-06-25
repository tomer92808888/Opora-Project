# Importing the essential libraries
import pandas as pd

class Laps():
    def __init__(self, laps):
        """
        Initializes the class with the given laps and if there are no lips it will create a new dataframes with 0 as values to make sure that the calculations will work
        """
        if laps.empty:
            self.LAPS = pd.DataFrame({'lap': [0],'milliseconds': [0]})
        else:
            self.LAPS = laps
    
    def get_laps(self) -> pd.DataFrame:
        """
        Returns the laps dataframe
        """
        return self.LAPS
    
    def milliseconds_to_time(self, milliseconds) -> str:
        """
        Converts the given milliseconds to a time format
        """
        minutes= int((milliseconds/(1000*60))%60)
        seconds= int((milliseconds/1000)%60)
        milliseconds = int(milliseconds%1000)
        return str(minutes) + ':' + str(seconds) + '.' + str(milliseconds)

    def get_average_lap_time(self) -> float:
        """
        Returns the average lap time
        """
        return self.milliseconds_to_time(self.get_laps()['milliseconds'].mean())

    def get_fastest_lap_time(self):
        """
        Returns the fastest lap time and the lap it was on
        """
        fastest_milliseconds = (self.get_laps()['milliseconds'].min())
        fastest_lap = self.get_laps()[self.get_laps()['milliseconds'] == fastest_milliseconds]['lap'].values[0]
        return self.milliseconds_to_time(fastest_milliseconds), fastest_lap

    def get_slowest_lap_time(self):
        """
        Returns the slowest lap time and the lap it was on
        """
        slowest_milliseconds = (self.get_laps()['milliseconds'].max())
        slowest_lap = self.get_laps()[self.get_laps()['milliseconds'] == slowest_milliseconds]['lap'].values[0]
        return self.milliseconds_to_time(slowest_milliseconds), slowest_lap