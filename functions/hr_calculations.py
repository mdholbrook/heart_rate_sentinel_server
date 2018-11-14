from datetime import datetime
import time


def append_heart_rate(df, database):
    """Appends the input heart rate to the patient in the database

    Args:
        df (dict): input dictionary of patient_id and heart_rate
        database (list of dict): list containing all patient data

    Returns:
        list: updates database to include the send heart rate
    """

    # Get patient index in database
    ind = find_id_ind(df['patient_id'], database)

    # Append heart rate to database
    database[ind]['heart_rate'].append(df['heart_rate'])

    # Append timestamp
    timestamp = create_timestamp()
    database[ind]['time'].append(timestamp)

    message = 'Added the heart rate %d to patient %s at %s' \
              % (df['heart_rate'], df['patient_id'], timestamp)
    print(message)

    return database


def find_id_ind(p_id, database):
    """Finds the index of the input patient in the database

    Args:
        p_id (str): the input patient ID
        database (list of dict): Contains all entered patients

    Returns:

    """

    # Get a list of IDs in database
    ids = [database[i]['patient_id'] for i in range(len(database))]

    # Find index of current ID
    try:
        inds = ids.index(p_id)

    except ValueError:
        raise ValueError('The input ID (%s) is not in the database!' % p_id)

    return inds


def get_heart_rates(p_id, database):
    """Takes a patient ID and returns all recorded heart rate information

    Args:
        p_id (str): the patient ID to use for heart rate retrieval
        database (list of dict): the database containing all patient
            information

    Returns:
        list: a list of all heart rates recorded for a given patient
    """

    # Get index in list for patient
    ind = find_id_ind(p_id, database)

    # Return stored heart rate measurements
    return database[ind]['heart_rate']


def create_timestamp():
    """Creates a timestamp for the heart rate measurement

    Returns:
        str: date and time, eg. "2018-03-09 11:00:36.372339"
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def average_heart_rate(heart_rates):
    """Calculate the average of a list of heart rates

    Args:
        heart_rates (list): a list of heart rates

    Returns:
        float: the average heart rate
    """
    # Compute sum and length of the input list
    hr_sum = sum(heart_rates)
    hr_length = len(heart_rates)

    return hr_sum/hr_length


def get_date_as_numeric(date):
    """Takes the date as a string and returns it as a float
    The input date is converted to seconds for comparison with other dates

    Args:
        date (str): the date as a string "%Y-%m-%d %H:%M:%S.%f",
        eg "2018-03-09 11:00:36.372339"

    Returns:
        float: time in seconds
    """
    # Expression to match
    expression = "%Y-%m-%d %H:%M:%S.%f"

    # Convert date to seconds
    seconds = time.mktime(datetime.strptime(date, expression).timetuple())

    return seconds
