# Importing the essential libraries
import json

# Importing the essential classes
from Season import Season
from Driver import Driver


class API_Functions():
    def drivers_by_season(self, season) -> json:
        """
        Returns a json of all drivers in the given season
        """
        SEASON = Season(season)
        json_data = SEASON.get_sorted_by_wins().to_json(orient="index")
        return json.loads(json_data)

    def seasons_all_time_ranking(self, season) -> json:
        """
        Returns a json of the top 3 drivers in the given season
        """
        SEASON = Season(season)
        json_data = SEASON.get_top_3().to_json(orient="index")
        return json.loads(json_data)

    def driver_profile(self, driver_id_or_name) -> json:
        """
        Returns a json of the driver's profile
        """
        DRIVER = Driver(driver_id_or_name)
        json_data = DRIVER.driver_profile().to_json(orient="index")
        return json.loads(json_data)
