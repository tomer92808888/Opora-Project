# Importing the essential libraries
import pandas as pd

# Importing the essential classes
from Data import Data
from Laps import Laps
from Pit_Stops import Pit_Stops

# Getting the preprocessed data
data = Data('csv')
data.get_csv_names()
DATA = data.clean()



class Personal_Race():
    def __init__(self, driver_id, race_id):
        """
        Initializes the class with given driver_id
        """
        self.DRIVER_ID = driver_id
        self.RACE_ID = race_id
        
        laps = DATA['lap_times'][(DATA['lap_times']['driverId'] == self.DRIVER_ID) & (DATA['lap_times']['raceId'] == self.RACE_ID)][['lap','milliseconds']]
        self.LAPS = Laps(laps)

        name = DATA['drivers'][DATA['drivers']['driverId'] == self.DRIVER_ID][['forename', 'surname']]
        self.NAME = " ".join(name.values[0])

        pit_stops = DATA['pit_stops'][(DATA['pit_stops']['driverId'] == self.DRIVER_ID) & (DATA['pit_stops']['raceId'] == self.RACE_ID)][['stop','milliseconds']]
        self.PIT_STOPS = Pit_Stops(pit_stops)

        circuit_id = DATA['races'][DATA['races']['raceId'] == self.RACE_ID]['circuitId'].values[0]
        self.CIRCUIT = DATA['circuits'][DATA['circuits']['circuitId'] == circuit_id]['name'].values[0]

        self.POINTS = DATA['results'][(DATA['results']['driverId'] == self.DRIVER_ID) & (DATA['results']['raceId'] == self.RACE_ID)]['points'].values[0].astype(int)

        self.POSITION = DATA['results'][(DATA['results']['driverId'] == self.DRIVER_ID) & (DATA['results']['raceId'] == self.RACE_ID)]['position'].values[0]

        self.SEASON = DATA['races'][DATA['races']['raceId'] == self.RACE_ID]['year']

    def get_name(self) -> str:
        """
        Returns the name of the driver
        """
        return self.NAME

    def get_season(self) -> int:
        """
        Returns the season in which the driver participated in
        """
        return self.SEASON

    def get_driver_id(self) -> int:
        """
        Returns the driver's ID
        """
        return self.DRIVER_ID
    
    def get_race_id(self) -> int:
        """
        Returns the race's ID
        """
        return self.RACE_ID

    def get_position(self) -> int:
        """
        Returns the position of the driver in the current race
        """
        return self.POSITION

    def get_points(self) -> int:
        """
        Returns the points that driver received in the current race
        """
        return self.POINTS

    def get_circuit(self) -> str:
        """
        Returns the circuit in which the driver participated in
        """
        return self.CIRCUIT

    def get_laps(self):
        """
        Returns the Lap class of the driver in the current race
        """
        return self.LAPS

    def get_pit_stops(self):
        """
        Returns the Pit_Stops class of the driver in the current race
        """
        return self.PIT_STOPS

    def get_average_lap_time(self) -> float:
        """
        Returns the average lap time of the driver in the current race
        """
        return self.get_laps().get_average_lap_time()
    
    def get_fastest_lap_time(self):
        """
        Returns the fastest lap time of the driver in the current race
        """
        return self.get_laps().get_fastest_lap_time()

    def get_slowest_lap_time(self):
        """
        Returns the slowest lap time of the driver in the current race
        """
        return self.get_laps().get_slowest_lap_time()

    def get_number_of_pit_stops(self) -> int:
        """
        Returns the number of pits stops that driver made in current race
        """
        return self.get_pit_stops().number_of_pit_stops()

    def get_fastest_pit_stop(self):
        """
        Returns the fastest pit stop of the driver in the current race
        """
        return self.get_pit_stops().get_fastest_pit_stop()

    def get_slowest_pit_stop(self):
        """
        Returns the slowest pit stop of the driver in the current race
        """
        return self.get_pit_stops().get_slowest_pit_stop()

    def get_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({"Driver ID": self.get_driver_id(), "Driver Name": self.get_name() ,"Race ID": self.get_race_id(), "Season": self.get_season(),
                             "Average Lap Time": self.get_average_lap_time(), "Fastest Lap Number": self.get_fastest_lap_time()[1] , "Fastest Lap Time": self.get_fastest_lap_time()[0] , "Slowest Lap Number": self.get_slowest_lap_time()[1], "Slowest Lap Time": self.get_slowest_lap_time()[0] , 
                             "Number of pits stops": self.get_number_of_pit_stops(), "Fastest Pit Stop Number": self.get_fastest_pit_stop()[1] , "Fastest Pit Stop Duration": self.get_fastest_pit_stop()[0] , "Slowest Pit Stop Number": [self.get_slowest_pit_stop()[1]], "Slowest Pit Stop Duration": [self.get_slowest_pit_stop()[0]],
                             "Circuit": self.get_circuit(), "Points": self.get_points(), "Position": self.get_position()})