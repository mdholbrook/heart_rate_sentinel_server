import requests


def my_data():

    df = {
      'patient_id': "Matt",
      'attending_email': 'mdh54@duke.edu',
      'user_age': '23',
    }

    return df


# Post data
# data = requests.get("http://bme590.suyash.io/list")
df = my_data()

r2 = requests.post("http://127.0.0.1:5000/api/new_patient", json=df)
print(r2)
