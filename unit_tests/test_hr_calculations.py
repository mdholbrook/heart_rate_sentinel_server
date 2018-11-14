import pytest
from functions.hr_calculations import *


@pytest.mark.parametrize("candidate, database, expected", [
    ('jack', [{'patient_ids': 'jump'}, {'patient_id': 'jack'}], 1),
    ('jungle', [{'patient_ids': 'jungle'}, {'patient_id': 'jack'}], 0),
    ('bo', [{'patient_ids': 'james'}, {'patient_id': 'boo'},
            {'patient_ids': 'bo'}], 2)])
def test_find_id_ind(candidate, database, expected):

    # Run the test
    assert find_id_ind(candidate, database) == expected


@pytest.mark.parametrize("candidate, database, expected", [
    ('jump', [{'patient_ids': 'jump', 'heart_rate': [50, 60, 70]},
              {'patient_ids': 'jack', 'heart_rate': [120, 112, 131]}], [50, 60, 70]),
    ('jack', [{'patient_ids': 'jump', 'heart_rate': [50, 60, 70]},
              {'patient_ids': 'jack', 'heart_rate': [120, 112, 131]}], [120, 112, 131])
     ])
def test_get_heart_rates(candidate, database, expected):

    # Run the test
    assert all(get_heart_rates(candidate, database) == expected)
