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


def find_id_ind(id, database):
    """Finds the index of the input patient in the database

    Args:
        id (str): the input patient ID
        database (list of dict): Contains all entered patients

    Returns:

    """

    # Get a list of IDs in database
    ids = [database[i]['patient_ids'] for i in range(len(database))]

    # Find index of current ID
    try:
        inds = ids.index(id)

    except ValueError:
        raise ValueError('The input ID (%s) is not in the database!' % id)

    return inds
