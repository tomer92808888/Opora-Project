# Importing the essential libraries
import os
import pandas as pd

class Data():
    def __init__(self, folder):
        """
        Initializes the class with a folder name of all the datasets
        """
        self.FOLDER = folder
    
    def get_folder(self) -> str:
        """
        Returns the folder name
        """
        return self.FOLDER

    def get_csv_names(self) -> list:
        """
        Returns a list of all the csv file names in the folder
        """
        csv_names = []
        for file in os.listdir(self.get_folder()):
            if file.endswith('.csv'):
                csv_names.append(file)
        return csv_names

    def get_csv_dict(self) -> dict:
        """
        Returns a dictionary of all the csv files in the folder, {'csv_name': csv_data}
        """
        csv_names = self.get_csv_names()
        self.csv_dict = {}
        for name in csv_names:
            self.csv_dict[name[:-4]] = pd.read_csv('csv/' + name)
        return self.csv_dict

    def clean(self) -> dict:
        """
        Replaces the NaN values with 0 so that the data can be used in the later calculations
        """
        self.get_csv_dict()['results'] = self.get_csv_dict()['results'].replace(r"\N", 0)
        return self.csv_dict

