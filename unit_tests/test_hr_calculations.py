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

    # Run the test
    assert pytest.approx(average_heart_rate(candidate), 1e-2) == expected


@pytest.mark.parametrize("candidate", [
    '2018-03-09 11:00:36.372339',
    '2017-10-19 15:11:36.167854',
    ])
def test_get_date_as_numeric(candidate):

    # Run the test
    result = pytest.approx(get_date_as_numeric(candidate), rel=1e-6)

    # Generate expected result
    expression = "%Y-%m-%d %H:%M:%S.%f"
    expected = datetime.strptime(candidate, expression).timestamp()

    assert result == expected


@pytest.mark.parametrize("candidate, expected", [
    ('Mark', ['2018-03-09 11:00:36.372339', '2017-10-19 15:11:36.167854']),
    ('Matt', ['2018-03-10 11:00:32.372339', '2017-10-19 35:11:36.167854'])
    ])
def test_get_times(candidate, expected):
    database = [{'patient_id': 'Mark', 'time':
                ['2018-03-09 11:00:36.372339', '2017-10-19 15:11:36.167854']},
                {'patient_id': 'Matt', 'time':
                ['2018-03-10 11:00:32.372339', '2017-10-19 35:11:36.167854']}]

    # Run the test
    assert get_times(candidate, database) == expected


@pytest.mark.parametrize("ref_time, times, hr, expected", [
    ('2018-03-09 11:00:36.372339',
     ['2018-03-09 11:00:34.372339',
      '2018-03-09 11:00:35.372339',
      '2018-03-09 11:00:36.872339'], [0, 0, 0], [0]),
    ('2018-03-09 11:00:36.372339',
     ['2018-03-09 11:00:35.372339',
      '2018-03-09 11:00:36.372359',
      '2018-03-09 11:00:37.372339'], [0, 0, 0], [0, 0])])
def test_hr_after_time(ref_time, times, hr, expected):

    # Run the test
    assert hr_after_time(ref_time, times, hr) == expected


@pytest.mark.parametrize("times, ref_time, expected", [
    ([0, 1, 2, 3, 4], 3, 4),
    ([0, 1, 2, 3, 4], 2.5, 3),
    ([0, 1, 2, 3, 4], 1.5, 2)
    ])
def test_find_index_larger(ref_time, times, expected):

    # Run the test
    assert find_index_larger(times, ref_time) == expected


@pytest.mark.parametrize("times, ref_time, expected", [
    ([0, 1, 2, 3, 4], 3, True),
    ([0, 1, 2, 3, 4], 4, True),
    ([0, 1, 2, 3, 4], 4.5, False),
    ([0, 1, 2, 3, 4], 0, True)
    ])
def test_check_recent_timestamps(ref_time, times, expected):

    # Run the test
    assert check_recent_timestamps(times, ref_time) == expected
