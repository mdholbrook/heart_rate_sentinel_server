import logging
import re
logging.basicConfig(filename='server.log', level=logging.DEBUG)


def verify_new_patient(df, database):
    """verifies that new patient information is in the correct format

    This function tests that the input data is a dictionary, contains
    the required keys, has a valid email, and that the patient's age is a valid
    integer.

    Args:
        df (dict): input dictionary for a new patient
        database (list of dict): full list of patient data

    Returns:
        bool: True if passes all tests
    """

    # Find if df is a dictionary
    if not is_dictionary(df):
        logging.warning('Input new patient data is not a dictionary!')
        raise TypeError('Input new patient data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'attending_email', 'user_age']

    for required_key in required_keys:
        if not contains_key(required_key, df):
            logging.warning('Input new patient dictionary is missing key %s!'
                            % required_key)
            raise TypeError('Input new patient dictionary is missing key %s!'
                            % required_key)

    # Check that the email is valid
    email = df[required_keys[1]]
    if not valid_email(email):
        logging.warning('Input email address (%s) is invalid!'
                        % email)
        raise ValueError('Input email address (%s) is invalid!'
                         % email)

    # Check that age is a valid number, convert to int
    age = df[required_keys[2]]
    t, df[required_keys[2]] = is_numeric(age)
    if not t:
        logging.warning('Input age (%s) must be an integer!' % age)
        TypeError('Input age (%s) must be an integer!' % age)

    # Check if patient exists in the database
    if len(database) > 0:
        p_id = df[required_keys[0]]
        if patient_is_in_database(p_id, database):
            logging.warning('The input patient ID (%s) is already in the '
                            'database!' % p_id)
            raise ValueError('The input patient ID (%s) is already in the '
                             'database!' % p_id)


def verify_input_hr(df, database):
    """verifies that new heart rate information is in the correct format

    This function tests that the input data is a dictionary, contains
    the required keys, has an existing patient ID, and that the heart rate is
    a valid integer.

    Args:
        df (dict): input dictionary for a new patient
        database (list of dict): full list of patient data

    Returns:
        bool: True if passes all tests
    """

    # Find if df is a dictionary
    if not is_dictionary(df):
        raise ValueError('Input data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'heart_rate']

    for required_key in required_keys:
        if not contains_key(required_key, df):
            logging.warning('Input dictionary is missing key %s!'
                            % required_key)
            raise ValueError('Input dictionary is missing key %s!'
                             % required_key)

    # Check that the heart rate is valid
    hr = df[required_keys[1]]
    if not hr_validation(hr):
        raise ValueError('Input heart rate (%d) is not within possible ranges!'
                         % hr)

    # Check that patient exists in the database
    if len(database) > 0:
        p_id = df[required_keys[0]]
        if not patient_is_in_database(p_id, database):
            raise ValueError('The input patient ID (%s) is not in the '
                             'database!' % p_id)
    else:
        raise LookupError('There are no patients entered in the directory!')


def verify_input_internal_average(df, database):
    """verifies that the data structures posted to the input_internal_average
     function is in the correct format

    This function tests that the input data is a dictionary, contains
    the required keys, has a valid email, and that the patient's age is a valid
    integer.

    Args:
        df (dict): input dictionary for a new patient
        database (list of dict): full list of patient data

    Returns:
        bool: True if passes all tests
    """

    # Find if df is a dictionary
    if not is_dictionary(df):
        logging.warning('Input data is not a dictionary!')
        raise ValueError('Input data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'heart_rate_average_since']

    for required_key in required_keys:
        if not contains_key(required_key, df):
            logging.warning('Input dictionary is missing key %s!'
                            % required_key)
            raise ValueError('Input dictionary is missing key %s!'
                             % required_key)

    # Check that patient exists in the database
    if len(database) > 0:
        p_id = df[required_keys[0]]
        if not patient_is_in_database(p_id, database):
            logging.warning('The input patient ID (%s) is not in the '
                            'database!' % p_id)
            raise ValueError('The input patient ID (%s) is not in the '
                             'database!' % p_id)
    else:
        logging.warning('There are no patients entered in the directory!')
        raise LookupError('There are no patients entered in the directory!')

    # Check that the date is in the correct format
    date = df[required_keys[1]]
    if not type(date) == str:
        logging.warning("Please enter the date as a string!")
        raise ValueError("Please enter the date as a string!")

    if not check_date_format(date):
        logging.warning("Entered date, %s, is not in the correct format.\n"
                        "Please enter date as: '2018-03-09 11:00:36.372339'")
        raise ValueError("Entered date, %s, is not in the correct format.\n"
                         "Please enter date as: '2018-03-09 11:00:36.372339'")


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
    """Checks if the input variable is numeric

    The function converts numeric strings and floats to int. If these
    processes fail, it returns a False flag which can be used for error
    handling.

    Args:
        num (int or float or float): input number

    Returns:
        bool, int: True if the input is numeric, the input returned as an
            integer
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
        bool: Boolean returns True if heart rate is within possible bounds
    """

    hr_upper_bound = 480    # Ventricular tachycardia
    hr_lower_bound = 0      # Deceased

    if hr_lower_bound <= hr < hr_upper_bound:
        return True

    else:
        return False


def patient_is_in_database(p_id, database):
    """This function searches the database for an input patient ID

    Args:
        p_id (str): patient ID
        database (list of dict): list containing all patient and heart rate
            information

    Returns:
        bool: Boolean value returns True if the patient is in the database
    """

    # Get a list of IDs in database
    ids = [database[i]['patient_id'] for i in range(len(database))]

    # Find index of current ID
    try:
        ids.index(p_id)

    except ValueError:
        return False

    return True


def check_date_format(date):
    """Checks the formatting of the posted date

    The date should be in the format: "%Y-%m-%d %H:%M:%S.%f" (eg.
    '2018-03-09 11:00:36.372339'). Returns False if this is not the case.

    Args:
        date (str): input date as a string

    Returns:
        bool: True is the date is in the correct format
    """

    # The expression to match
    expression = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}"

    # Find if the input date matches
    mObj = re.fullmatch(expression, date)

    if mObj:
        return True

    else:
        return False
