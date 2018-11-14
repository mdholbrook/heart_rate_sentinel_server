import re


def verify_new_patient(df):
    """verifies that new patient information is in the correct format

    This function tests that the input data is a dictionary, contains
    the required keys, has a valid email, and that the patient's age is a valid
    integer.

    Args:
        df (dict): input dictionary for a new patient

    Returns:
        bool: True if passes all tests
    """

    # Find if df is a dictionary
    if not is_dictionary(df):
        raise ValueError('Input new patient data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'attending_email', 'user_age']

    for required_key in required_keys:
        if not contains_key(required_key, df):
            raise ValueError('Input new patient dictionary is missing key %s!'
                             % required_key)

    # Check that the email is valid
    email = df[required_keys[1]]
    if not valid_email(email):
        raise ValueError('Input email address (%s) is invalid!'
                         % email)

    # Check that age is a valid number, convert to int
    age = df[required_keys[2]]
    t, df[required_keys[2]] = is_numeric(age)
    if not t:
        raise ValueError('Input age (%s) must be an integer!' % age)


def verify_input_hr(df, database):

    # Find if df is a dictionary
    if not is_dictionary(df):
        raise ValueError('Input heart rate data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'heart_rate']

    for required_key in required_keys:
        if not contains_key(required_key, df):
            raise ValueError('Input dictionary is missing key %s!'
                             % required_key)

    # Check that the heart rate is valid
    hr = df[required_keys[1]]
    if not hr_validation(hr):
        raise ValueError('Input heart rate (%d) is not within possible ranges!'
                         % hr)

    # Check that patient exists in the database
    p_id = df[required_keys[0]]
    if not patient_is_in_database(p_id, database):
        raise ValueError('The input ID (%s) is not in the database!' % p_id)


def is_dictionary(df):
    """Determine if an input varible is a dictionary

    Args:
        df: incoming dictionary

    Returns:
        bool: True if the input was a dictionary and False otherwise
    """

    t = type(df)

    if t == dict:
        return True

    else:
        return False


def contains_key(required_key, df):
    """Checks if the required key is found in the input dictionary

    Args:
        required_key (str): a required key
        df (dict): the input dictionary being checked

    Returns:
        bool: True if the input contains the required key and False otherwise
    """

    if required_key in df:
        return True

    else:
        return False


def valid_email(email):
    """Check if entered email address is valid

    This checks if the email address contains a "@" followed by a "."

    Args:
        email (str): input email address

    Returns:
        bool: True if the input is a valid email and False otherwise
    """
    # Ensure email is a string
    if not type(email) == str:
        return False

    # Find @ and . in the email address
    if re.match("[^@]+@[^@]+.[^@]+", email):
        return True

    else:
        return False


def is_numeric(num):
    """Checks if the input variable is numeric (int)

    Args:
        num:

    Returns:
        bool: True if the input is numeric or numeric
        num (int): the input returned as an integer
    """
    # Get data type
    t = type(num)

    # If the number was input as a string
    if t == str:
        if num.isnumeric():
            return True, int(num)

        else:
            return False, num

    else:
        return True, int(num)


def hr_validation(hr):
    """Validates that the given heart rate is within physiological ranges

    Source for heart rate bounds: https://iytmed.com/dangerous-heart-rate/

    Args:
        hr (int): input heart rate in bmp

    Returns:
        bool: True if heart rate is within possible bounds
    """

    hr_upper_bound = 480    # Ventricular tachycardia
    hr_lower_bound = 0      # Deceased

    if hr_lower_bound <= hr < hr_upper_bound:
        return True

    else:
        return False


def patient_is_in_database(p_id, database):

    # Get a list of IDs in database
    ids = [database[i]['patient_ids'] for i in range(len(database))]

    # Find index of current ID
    try:
        ids.index(p_id)

    except ValueError:
        return False

    return True
