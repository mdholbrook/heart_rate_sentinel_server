from datetime import datetime
import warnings


def append_heart_rate(df, database):
    """Appends the input heart rate to the patient in the database

    Args:
        df (dict): input dictionary of patient_id and heart_rate
        database (list of dict): list containing all patient data

    Returns:
        list of dict, int: updates database to include the heart rate, also
            return the index of the patient in the database so that the patient
            ID will not have to be found again for following calculations
    """

    # Get patient index in database
    ind = find_id_ind(df['patient_id'], database)

    # Append heart rate to database
    database[ind]['heart_rate'].append(df['heart_rate'])

    # Append timestamp
    timestamp = create_timestamp()
    database[ind]['time'].append(timestamp)
    df['time'] = timestamp

    message = 'Added the heart rate %d to patient %s at %s' \
              % (df['heart_rate'], df['patient_id'], timestamp)
    print(message)

    return database, ind


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
    seconds = datetime.strptime(date, expression).timestamp()

    return seconds


def get_times(p_id, database):
    """Retrieve the timestamps for each heart rate recorded

    Args:
        p_id (str): a string identifying the patient
        database (list of dict): contains all patient data

    Returns:
        list: a list of timestamps pertaining to the patient
    """

    # Get index in list for patient
    ind = find_id_ind(p_id, database)

    # Return stored heart rate measurements
    return database[ind]['time']


def hr_after_time(ref_time, timestamps, heart_rates):
    """Gather the heart rates after a reference point in time
    Converts string dates to a numeric in seconds, then checks that there are
    recorded values occurring after the reference time. Returns a list of heart
    rate measurements after ref_time.

    Args:
        ref_time (str): the date and time as input by the user
        timestamps (list): a list of strings of the timestamps denoting when
            heart rate information was encountered.
        heart_rates (list) : a list of recorded heart rates

    Returns:
        list: a list of heart rates recorded after ref_time
    """

    # Get input date as a numeric
    num_in_time = get_date_as_numeric(ref_time)

    # Get timestamps as a numeric
    num_time = []
    for dt in timestamps:
        num_time.append(get_date_as_numeric(dt))

    # Ensure that there are more recent timestamps than the ref_time
    t = check_recent_timestamps(num_time, num_in_time)
    if t:
        # Find first date after input date
        ind = find_index_larger(num_time, num_in_time)

        # Return the heart rate after ind
        return heart_rates[ind:]

    else:
        warnings.warn('\nInput time (%s) is larger than last recorded time '
                      '(%s)\nUsing last recorded time: %s'
                      % (ref_time, timestamps[-1], timestamps[-1]))

        return [heart_rates[-1]]


def find_index_larger(times, ref_time):
    """Returns the index of times whose value is just larger than ref_time

    Args:
        times (list): A list of floats denoting a datestring in seconds
        ref_time (float): A input date in seconds

    Returns:
        int: the index which is just larger than ref_time
    """

    return next(i[0] for i in enumerate(times) if i[1] > ref_time)


def check_recent_timestamps(times, ref_time):
    """Checks if the input time is too recent and precludes all measurements

    Args:
        times (list): list of times, in seconds float, in which recordings were
         made
        ref_time (float): input reference time in seconds

    Returns:
        bool: returns True if there are more recent measurements than ref_time
    """

    # Get last recorded time
    last_time = times[-1]

    # If the time is less recent than the ref_time
    if last_time < ref_time:
        return False

    else:
        return True
