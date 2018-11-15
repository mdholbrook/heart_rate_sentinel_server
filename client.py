from flask import Flask, jsonify, request
from functions.verify_inputs import verify_new_patient, verify_input_hr
from functions.verify_inputs import patient_is_in_database
from functions.verify_inputs import verify_input_internal_average
from functions.hr_calculations import append_heart_rate, get_heart_rates
from functions.hr_calculations import average_heart_rate, get_times
from functions.hr_calculations import hr_after_time
from functions.tachycardia import Tachycardic
from functions.email_service import send_tachycardia_email


app = Flask(__name__)

# Make database in global memory
database = []
tachy = Tachycardic()


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
    database, ind = append_heart_rate(inputs, database)

    # Check if the patient is tachycardic
    state, _ = tachy.is_tachycardic(inputs['patient_id'], database)

    # If True, send an alert to the attending physician
    if state:
        send_tachycardia_email(database[ind])

    return jsonify({'Success': 200})


@app.route('/api/heart_rate/internal_average', methods=['POST'])
def internal_average():
    """Calculates the average heart rate for a patient after a given timestamp

    This message receives a post in the following format:
    {
    "patient_id": "1",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339" // date string
    }

    The patient's recorded heart rates after "heart_rate_average_since" will be
    used for calculating an average. If there are no measurements after this
    point an warning is raised and the last recorded heart rate is returned.

    Returns:

    """
    global database

    # Get posted data
    inputs = request.get_json()

    # Verify json has the correct fields
    verify_input_internal_average(inputs, database)

    # Get heart rates and times
    ref_time = inputs['heart_rate_average_since']
    heart_rates = get_heart_rates(inputs['patient_id'], database)
    timestamps = get_times(inputs['patient_id'], database)

    # Return heart rates after the set time
    hr_after = hr_after_time(ref_time, timestamps, heart_rates)

    # Compute the average of the returned heart rates
    av_hr = average_heart_rate(hr_after)

    # Create output message
    message = {'average_heart_rate': av_hr}
    print('Average heart rate for patient %s since %s: %0.2f (%d measurements)'
          % (inputs['patient_id'], ref_time, av_hr, len(hr_after)))

    return jsonify(message), 200


@app.route('/api/status/<patient_id>', methods=['GET'])
def status(patient_id):
    """Checks whether the called patient is currently tachycardic

    Args:
        patient_id (str): MRN number of the patient

    Returns:

    """

    # Check if patient is in database
    if not patient_is_in_database(patient_id, database):
        message = {'message': 'Patient %s not found in the database!'
                              % patient_id}
    else:
        # Return if patient is tachycardic
        state, timestamp = tachy.is_tachycardic(patient_id, database)

        message = {'is_tachycardic': state, 'timestamp': timestamp}

    return jsonify(message)


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
