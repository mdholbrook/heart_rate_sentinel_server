from flask import Flask, jsonify, request


app = Flask(__name__)

# Make database in memory
database = []


@app.route('/api/new_patient', methods=['POST'])
def new_patient():
    """Registers a new patient
    This is called when the heart rate monitor is checked out with a new
    patient, and initializes the patient in the database.

    An example POST is:
    {
    "patient_id": "1", # usually this would be the patient MRN
    "attending_email": "suyash.kumar@duke.edu",
    "user_age": 50, # in years
    }
    """
    global database

    # Get posted data
    inputs = request.get_json()
    print(inputs)

    # Verify json has the correct fields

    # Create patient
    data = {'patient_id': inputs[0],
            'attending_email': inputs[1],
            'user_age': inputs[2]}

    database.append(data)


@app.route('/api/heart_rate', methods=['POST'])
def post_heart_rate():
    """Stores a heart rate measurement for a given patient.
    This is called to store a heart rate for a patient identified with
    patient_id.

    An example POST is:
    {
    "patient_id": "1", # usually this would be the patient MRN
    "heart_rate": 100
    }
    """
    global database

    # Get posted data
    inputs = request.get_json()

    # Verify json has the correct fields

    # Separate input
    inputs


@app.route('/api/heart_rate/internal_average', methods=['POST'])
def internal_average():
    """

    Returns:

    """
    global database

    # Get posted data
    inputs = request.get_json()

    # Verify json has the correct fields


@app.route('/api/status/<patient_id>', methods=['GET'])
def status(patient_id):
    """Checks whether the called patient is currently tachycardic

    Args:
        patient_id (str): MRN number of the patient

    Returns:

    """
    global database


@app.route('/api/heart_rate/<patient_id>', methods=['GET'])
def get_heart_rate(patient_id):
    """Shows all recorded heart rates for a patient

    Args:
        patient_id:

    Returns:

    """
    global database


@app.route('/api/heart_rate/average/<patient_id>', methods=['GET'])
def average(patient_id):
    """Stores average of all heart rates stored for a patient.

    Args:
        patient_id:

    Returns:

    """
    global database


if __name__ == "__main__":

    # app.run(host='0.0.0.0')
    app.run()
