from flask import Flask, jsonify, request
from functions.verify_inputs import verify_new_patient, verify_input_hr
from functions.verify_inputs import patient_is_in_database
from functions.hr_calculations import append_heart_rate, get_heart_rates
from functions.hr_calculations import average_heart_rate


app = Flask(__name__)

# Make database in global memory
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

    try:
        # Verify json has the correct fields
        verify_new_patient(inputs, database)

        # Add fields for timestamp and heart rate
        inputs['time'] = []
        inputs['heart_rate'] = []

        # Append patient list
        database.append(inputs)

        result = {
            "message": "Added %s successfully to the patient list"
                       % inputs["patient_id"]
        }
        print(result)

        return jsonify(result)

    except Exception as e:
        print(e)

        return jsonify({'Error': 'See traceback'})


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
    verify_input_hr(inputs, database)

    # Add to database
    append_heart_rate(inputs, database)

    return jsonify({'Success': 200})


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

    test = {'id': 'fun', 'rank': 5}

    return jsonify(test)


@app.route('/api/heart_rate/<patient_id>', methods=['GET'])
def get_heart_rate(patient_id):
    """Shows all recorded heart rates for a patient

    Args:
        patient_id (str): the patient ID to which to show recorded heart rates

    Returns:
        json: message showing all recorded heart rates for a patient
    """
    # Check if patient is in database
    if not patient_is_in_database(patient_id, database):
        message = {'message': 'Patient %s not found in the database!'
                              % patient_id}
    else:

        hr = get_heart_rates(patient_id, database)
        message = {'heart_rates': hr}

    return jsonify(message)


@app.route('/api/heart_rate/average/<patient_id>', methods=['GET'])
def average(patient_id):
    """Calculates the average heart rate for each patient.
    This function works on all of the recorded heart rates (bmp) for a given
    patient.

    Args:
        patient_id (str): the patient identifier

    Returns:
        json: returns a json dictionary with the average heart rate
    """
    # Check if patient is in database
    if not patient_is_in_database(patient_id, database):
        message = {'message': 'Patient %s not found in the database!'
                              % patient_id}
    else:

        # Get heart rates
        hr = get_heart_rates(patient_id, database)

        # Calculate average heart rate
        av_hr = average_heart_rate(hr)

        message = {'average_heart_rate': av_hr}

    return jsonify(message)


if __name__ == "__main__":

    # app.run(host='0.0.0.0')
    app.run()
