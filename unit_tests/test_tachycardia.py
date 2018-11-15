import pytest
from functions.tachycardia import Tachycardic


@pytest.mark.parametrize("candidate, expected", [
    ('Matt', False),
    ('Mike', True),
    ('Jean', False),
    ('James', True),
    ('Jan', True),
    ('Jim', True),
])
def test_is_tachycardic(candidate, expected):

    df = [
        {'patient_id': 'Matt', 'user_age': 16, 'heart_rate': [100, 90]},
        {'patient_id': 'Mike', 'user_age': 16, 'heart_rate': [100, 101]},
        {'patient_id': 'Jean', 'user_age': 1, 'heart_rate': [149]},
        {'patient_id': 'James', 'user_age': 1, 'heart_rate': [152]},
        {'patient_id': 'Jan', 'user_age': 10, 'heart_rate': [131]},
        {'patient_id': 'Jim', 'user_age': 4, 'heart_rate': [97, 138]},
    ]

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
    df = [
        {'patient_id': 'Matt', 'user_age': 16, 'heart_rate': [100, 90]},
        {'patient_id': 'Mike', 'user_age': 16, 'heart_rate': [100, 101]},
        {'patient_id': 'Jean', 'user_age': 1, 'heart_rate': [149]},
        {'patient_id': 'James', 'user_age': 1, 'heart_rate': [152]},
        {'patient_id': 'Jan', 'user_age': 10, 'heart_rate': [131]},
        {'patient_id': 'Jim', 'user_age': 4, 'heart_rate': [97, 138]},
    ]

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
    df = [
        {'patient_id': 'Matt', 'user_age': 16, 'heart_rate': [100, 90]},
        {'patient_id': 'Mike', 'user_age': 16, 'heart_rate': [100, 101]},
        {'patient_id': 'Jean', 'user_age': 1, 'heart_rate': [149]},
        {'patient_id': 'James', 'user_age': 1, 'heart_rate': [152]},
        {'patient_id': 'Jan', 'user_age': 10, 'heart_rate': [131]},
        {'patient_id': 'Jim', 'user_age': 4, 'heart_rate': [97, 138]},
    ]

    tach = Tachycardic()

    assert tach.get_heart_rate(df, candidate) == expected
