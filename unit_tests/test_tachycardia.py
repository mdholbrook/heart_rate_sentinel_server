import pytest
from functions.tachycardia import Tachycardic

df = [
    {'patient_id': 'Matt', 'user_age': 16, 'heart_rate': [100, 90],
     'time': ['2018-03-09 11:00:35.372339', '2018-03-09 11:00:36.372339']},
    {'patient_id': 'Mike', 'user_age': 16, 'heart_rate': [100, 101],
     'time': ['2018-03-09 11:00:35.372339', '2018-03-09 11:00:35.372339']},
    {'patient_id': 'Jean', 'user_age': 1, 'heart_rate': [149],
     'time': ['2018-03-09 11:00:34.372339']},
    {'patient_id': 'James', 'user_age': 1, 'heart_rate': [152],
     'time': ['2018-03-09 11:00:33.372339']},
    {'patient_id': 'Jan', 'user_age': 10, 'heart_rate': [131],
     'time': ['2018-03-09 11:00:32.372339']},
    {'patient_id': 'Jim', 'user_age': 4, 'heart_rate': [97, 138],
     'time': ['2018-03-09 11:00:35.372339', '2018-03-09 11:00:31.372339']},
]


@pytest.mark.parametrize("candidate, expected", [
    ('Matt', (False, '2018-03-09 11:00:36.372339')),
    ('Mike', (True, '2018-03-09 11:00:35.372339')),
    ('Jean', (False, '2018-03-09 11:00:34.372339')),
    ('James', (True, '2018-03-09 11:00:33.372339')),
    ('Jan', (True, '2018-03-09 11:00:32.372339')),
    ('Jim', (True, '2018-03-09 11:00:31.372339')),
])
def test_is_tachycardic(candidate, expected):

    tach = Tachycardic()

    assert tach.is_tachycardic(candidate, df) == expected


@pytest.mark.parametrize("candidate, expected", [
    (0, 16),
    (1, 16),
    (2, 1),
    (3, 1),
    (4, 10),
    (5, 4),
])
def test_find_age(candidate, expected):

    tach = Tachycardic()

    assert tach.find_age(df, candidate) == expected


@pytest.mark.parametrize("candidate, expected", [
    (0, 90),
    (1, 101),
    (2, 149),
    (3, 152),
    (4, 131),
    (5, 138),
])
def test_get_heart_rate(candidate, expected):

    tach = Tachycardic()

    assert tach.get_heart_rate(df, candidate) == expected


@pytest.mark.parametrize("candidate, expected", [
    (0, '2018-03-09 11:00:36.372339'),
    (1, '2018-03-09 11:00:35.372339'),
    (2, '2018-03-09 11:00:34.372339'),
    (3, '2018-03-09 11:00:33.372339'),
    (4, '2018-03-09 11:00:32.372339'),
    (5, '2018-03-09 11:00:31.372339'),
])
def test_get_timestamp(candidate, expected):

    tach = Tachycardic()

    assert tach.get_timestamp(df, candidate) == expected
