import pytest
from functions.verify_inputs import *


@pytest.mark.parametrize("candidate, expected", [
    ('test', False),
    ([1, 3, 4, 2], False),
    ({'test': 'dict'}, True)])
def test_is_dictionary(candidate, expected):

    # Run the test
    assert is_dictionary(candidate) == expected


@pytest.mark.parametrize("required_key, dict, expected", [
    ('places', {'people': 'mark', 'places': 'SLC', }, True),
    ('places', {'people': 'mark', 'things': 'apples', }, False),
    ('funds', {'funds': [10, 12, 5.1], 'things': 'apples', }, True)
    ])
def test_contains_key(required_key, dict, expected):

    # Run the test
    assert contains_key(required_key, dict) == expected


@pytest.mark.parametrize("candidate, expected, expected_int", [
    (5, True, 5),
    (6.2, True, 6),
    ('Summer', False, 'Summer'),
    ('3', True, 3),
    ('9.2', False, '9.2')
    ])
def test_is_numeric(candidate, expected, expected_int):

    # Run the test
    t, num = is_numeric(candidate)

    assert t == expected
    assert num == expected_int


@pytest.mark.parametrize("candidate, expected", [
    (12, False),
    ('jim@jim.edu', True),
    ('jim.jim.edu', False),
    ("o'hare@gmail.com", True),
    ('9.2', False)
    ])
def test_is_numeric(candidate, expected):

    # Run the test
    assert valid_email(candidate) == expected


@pytest.mark.parametrize("candidate, expected", [
    (60, True),
    (0, True),
    (-1, False),
    (120, True),
    (500, False)
    ])
def test_hr_validation(candidate, expected):

    # Run the test
    assert hr_validation(candidate) == expected


@pytest.mark.parametrize("candidate, database, expected", [
    ('jack', [{'patient_id': 'jump'}, {'patient_id': 'jack'}], True),
    ('jungle', [{'patient_id': 'jungle'}, {'patient_id': 'jack'}], True),
    ('john', [{'patient_id': 'james'}], False)])
def test_patient_is_in_database(candidate, database, expected):

    # Run the test
    assert patient_is_in_database(candidate, database) == expected


@pytest.mark.parametrize("candidate, expected", [
    ('January 31st, 2016', False),
    ('2018-06-01 11:59:99.999999', True),
    ('test', False)])
def test_check_date_format(candidate, expected):

    # Run the test
    assert check_date_format(candidate) == expected
