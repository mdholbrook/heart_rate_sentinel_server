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

    return database


def find_id_ind(p_id, database):
    """Finds the index of the input patient in the database

    Args:
        p_id (str): the input patient ID
        database (list of dict): Contains all entered patients

    Returns:

    """

    # Get a list of IDs in database
    ids = [database[i]['patient_ids'] for i in range(len(database))]

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
