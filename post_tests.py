import requests
import numpy as np
import time
from datetime import datetime, timedelta


def my_data1():
    df = {
      'patient_id': "Matt",
      'attending_email': 'mdh54@duke.edu',
      'user_age': '23',
    }
    return df


def my_data2():
    df = {
      'patient_id': "Mike",
      'attending_email': 'mdh54@duke.edu',
      'user_age': '25',
    }
    return df


def add_heart_rate1():

    hr = np.random.randint(40, 100)

    df = {'heart_rate': hr, 'patient_id': 'Matt'}

    return df


def add_heart_rate2():

    hr = np.random.randint(100, 140)

    df = {'heart_rate': hr, 'patient_id': 'Mike'}

    return df


def post_new_patient_data():

    df = my_data1()
    r = requests.post("http://127.0.0.1:5000/api/new_patient", json=df)
    print(r)

    df = my_data2()
    r = requests.post("http://127.0.0.1:5000/api/new_patient", json=df)
    print(r)


def post_heart_rate_data():

    for _ in range(60):
        time.sleep(0.2)
        df = add_heart_rate1()
        r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=df)
        print(r)

        time.sleep(0.2)
        df = add_heart_rate2()
        r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=df)
        print(r)


def post_interval():

    expression = "%Y-%m-%d %H:%M:%S.%f"
    date = datetime.now()
    subtract = timedelta(seconds=10)  # 1 second
    c = date - subtract
    c = c.strftime(expression)

    df = {
        "patient_id": "Mike",
        "heart_rate_average_since": c
        }
    time.sleep(0.1)
    r = requests.post(
        "http://127.0.0.1:5000/api/heart_rate/internal_average", json=df)
    print(r)


if __name__ == "__main__":

    post_new_patient_data()

    post_heart_rate_data()

    post_interval()

    # post_heart_rate_data()
