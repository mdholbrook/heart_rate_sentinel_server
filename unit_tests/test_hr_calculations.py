import pytest
from functions.hr_calculations import *


@pytest.mark.parametrize("candidate, database, expected", [
    ('jack', [{'patient_ids': 'jump'}, {'patient_ids': 'jack'}], 1),
    ('jungle', [{'patient_ids': 'jungle'}, {'patient_ids': 'jack'}], 0),
    ('bo', [{'patient_ids': 'james'}, {'patient_ids': 'boo'},
            {'patient_ids': 'bo'}], 2)])
def test_find_id_ind(candidate, database, expected):

    # Run the test
    assert find_id_ind(candidate, database) == expected
