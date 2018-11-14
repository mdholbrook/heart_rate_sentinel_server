import re


def verify_new_patient(dict):
    """verifies that new patient information is in the correct format

    This function tests that they input dictionary is a dictionary, contains
    the required keys, has a valid email, and that the patient's age is a valid
    integer.

    Args:
        dict (dict): input dictionary for a new patient

    Returns:
        bool: True if passes all tests
    """

    # Find if dict is a dictionary
    if not is_dictionary(dict):
        raise ValueError('Input data is not a dictionary!')

    # Ensure the required keys exist
    required_keys = ['patient_id', 'attending_email', 'user_age']

    for required_key in required_keys:
        if contains_key(required_key, dict):
            raise ValueError('Input dictionary is missing key %s!'
                             % required_key)

    # Check that the email is valid
    email = dict[required_keys[1]]
    if not valid_email(email):
        raise ValueError('Input email address (%s) is invalid!'
                         % email)

    # Check that age is a valid number, convert to int
    age = dict[required_keys[3]]
    t, dict[required_keys[3]] = is_numeric(age)
    if not t:
        raise ValueError('Input age (%s) must be an integer!' %age)


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


def contains_key(required_key, dict):
    """Checks if the required key is found in the input dictionary

    Args:
        required_key (str): a required key
        dict (dict): the input dictionary being checked

    Returns:
        bool: True if the input contains the required key and False otherwise
    """

    if required_key in dict:
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
