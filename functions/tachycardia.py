import pandas as pd


class Tachycardic:
    def __init__(self):
        # Assign data directory
        data_dir = 'functions/tachy_data.csv'

        # Load reference data
        self.df = pd.read_csv(data_dir)

    def is_tachycardic(self, data):

        # Find the patient age and heart rate
        age = data['user_age']
        hr = data['heart_rate']

        # Find patient age range
        age_ind = (self.df['Year1'] <= age) & \
                  (age <= self.df['Year2'])

        # Determine if the patient is tachycardic
        if hr > self.df['BMP'][age_ind]:
            return True

        else:
            return False
