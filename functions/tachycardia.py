import pandas as pd
from functions.hr_calculations import find_id_ind


class Tachycardic:
    def __init__(self):
        # Assign data directory
        data_dir = 'functions/tachy_data.csv'

        # Load reference data
        self.df = pd.read_csv(data_dir)

    def is_tachycardic(self, patient_id, database):

        # Get the patient from the database
        ind = find_id_ind(patient_id, database)

        # Find the patient age and latest heart rate
        age = database[ind]['user_age']
        hr = database[ind]['heart_rate'][-1]

        # Find patient age range
        age_ind = (self.df['Year1'] <= age) & \
                  (age <= self.df['Year2'])
        thresh_hr = int(self.df['BMP'][age_ind])

        # Determine if the patient is tachycardic
        if hr > thresh_hr:
            return True

        else:
            return False
