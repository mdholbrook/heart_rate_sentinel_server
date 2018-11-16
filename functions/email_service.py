import sendgrid
import os
from sendgrid.helpers.mail import *


def send_tachycardia_email(df):
    """Sends an email to the attending physician

    The email warns of a tachycardic heart rate and includes the patient ID,
    age, current heart rate, and the time that the heart rate was recorded.

    Args:
        df (dict): dictionary containing the tachycardic patient information
            and heart rate data.

    Returns:
        None
    """

    # Set up email
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("automatic_alert@heartratesentinal.com")
    to_email = Email(df['attending_email'])

    # Set up email subject
    subject = "TACHYCARDIA ALERT: %s" % df['patient_id']

    # Set up email body
    body = Content("text/plain", "Patient: %s "
                                 "(age: %s\n) has a heart rate of "
                                 "%s at %s"
                                 % (df['patient_id'],
                                    df['user_age'],
                                    df['heart_rate'][-1],
                                    df['time'][-1]))

    # Send email
    mail = Mail(from_email, subject, to_email, body)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
