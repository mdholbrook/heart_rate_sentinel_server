import pandas as pd
from functions.hr_calculations import find_id_ind


class Tachycardic:
    def __init__(self):
        # Assign data directory
        data_dir = 'functions/tachy_data.csv'

        # Load reference data
        self.df = pd.read_csv(data_dir)

    def is_tachycardic(self, patient_id, database):
        """Computes if the patient is tachycardic
        This function finds the patient in the datebase, grabs the last heart
        rate recorded, and uses the patient's age to determine if the patient
        is tachycardic

        Args:
            patient_id (str): patient identifier
            database (list of dict): a list of patients and their information

        Returns:
            bool: True if the patient is tachycardic, false otherwise
        """

        # Get the patient from the database
        ind = find_id_ind(patient_id, database)

        # Find the patient age and latest heart rate
        age = self.find_age(database, ind)
        hr = self.get_heart_rate(database, ind)

        # Find patient age range
        age_ind = (self.df['Year1'] <= age) & \
                  (age <= self.df['Year2'])
        thresh_hr = int(self.df['BMP'][age_ind])

        # Determine if the patient is tachycardic
        if hr > thresh_hr:
            return True

        else:
            return False

    def find_age(self, database, ind):
        """Finds the patient's age

        Args:
            database (list of dict): a list of patients and their information
            ind (int): the index of the patient in database

        Returns:
            int: the users age in years
        """

        return database[ind]['user_age']

    def get_heart_rate(self, database, ind):
        """Finds the patient's last heart rate

        Args:
            database (list of dict): a list of patients and their information
            ind (int): the index of the patient in database

        Returns:
            int: the last recorded heart rate for the patient
        """

        return database[ind]['heart_rate'][-1]
