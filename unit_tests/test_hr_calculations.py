import pytest
from functions.hr_calculations import *


@pytest.mark.parametrize("candidate, database, expected", [
    ('jack', [{'patient_id': 'jump'}, {'patient_id': 'jack'}], 1),
    ('jungle', [{'patient_id': 'jungle'}, {'patient_id': 'jack'}], 0),
    ('bo', [{'patient_id': 'james'}, {'patient_id': 'boo'},
            {'patient_id': 'bo'}], 2)])
def test_find_id_ind(candidate, database, expected):

    # Run the test
    assert find_id_ind(candidate, database) == expected


@pytest.mark.parametrize("candidate, database, expected", [
    ('jump', [{'patient_id': 'jump', 'heart_rate': [50, 60, 70]},
              {'patient_id': 'jack', 'heart_rate': [120, 112, 131]}],
     [50, 60, 70]),
    ('jack', [{'patient_id': 'jump', 'heart_rate': [50, 60, 70]},
              {'patient_id': 'jack', 'heart_rate': [120, 112, 131]}],
     [120, 112, 131])
     ])
def test_get_heart_rates(candidate, database, expected):

    # Run the test
    assert get_heart_rates(candidate, database) == expected


@pytest.mark.parametrize("candidate, expected", [
    ([50, 60, 70], 60),
    ([50, 55, 56], 53.66),
    ([0, 50, 100], 50),
    ])
def test_average_heart_rate(candidate, expected):

    assert pytest.approx(average_heart_rate(candidate), 1e-2) == expected


@pytest.mark.parametrize("candidate, expected", [
    ('2018-03-09 11:00:36.372339', 1520611236.372339),
    ('2017-10-19 15:11:36.167854', 1508440296.167854),
    ])
def test_get_date_as_numeric(candidate, expected):

    assert get_date_as_numeric(candidate) == expected
