

# Heart Rate Sentinel Server


A simple centralized heart rate sentinel server. This server will be built to receive POST requests from mock patient heart rate monitors that contain patient heart rate information over time. If a patient exhibits a tachycardic heart rate, the physician should receive an email warning them. This calculation should be based on age and heart rate.

#### Travis contiuous integration status
[![Build Status](https://travis-ci.com/mdholbrook/heart_rate_sentinel_server.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)


Welcome to the Heart Rate Sentinel Server project. This is an open-source project which can be
used to process patient heart rate data to make informed health care decisions. This project is
part of the coursework for the Fall 2018 BME 590 - Medical Software Design at Duke University.

The RESTful API for this project is set up to provide interactions via a web service.
POST requests using ``/api/new_patient`` can be made containing new patient
information, including the patient's ID, age, and attending physician's email address.
Heart rate information can then be posted to the server using ``/api/heart_rate``
where it is stored. Calculations are made
for each posted heart to determine if the patient is in a tachycardic state. If they are tachycardic
an alert is sent to the attending physician's email. An average heart rate since a
given time will be calculated using a POST to ``/api/heart_rate/interval_average``.

The RESTful API can return heart rate information using GET requests. A full list of recorded heart
rates can received using ``/api/heart_rate/<patient_id>``, where ``<patient_id>`` is the ID specific to
a particular patient. These ID are **case sensitive**. An average heart rate can be returned using
the ``/api/heart_rate/average/<patient_id>`` GET request. The patient's tachycardic state will be returned
using ``/api/status/<patient_id>``.