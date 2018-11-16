
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/mdholbrook/heart_rate_sentinel_server.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

# Heart Rate Sentinel Server

### General information
This project represents a simple centralized heart rate sentinel server. This server has been built to receive POST requests from mock patient heart rate monitors that contain patient heart rate information over time. If a patient exhibits a tachycardic heart rate, the physician should receive an email warning them. This calculation should be based on age and heart rate.


## About the heart rate sentinel project

Welcome to the Heart Rate Sentinel Server project. This is an open-source project which can be
used to process patient heart rate data to make informed health care decisions. This project is
part of the coursework for the Fall 2018 BME 590 - Medical Software Design at Duke University.

The [API Documentation](https://htmlpreview.github.io/?https://github.com/mdholbrook/heart_rate_sentinel_server/blob/master/docs/_build/html/index.html) describes may of the RESTfil API interfaces and functions used in this project.


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

## How to access the server

The python script ``client.py`` runs a flask server. This can be run locally or remotely. The server is currently running on a virtual machine located at ``http://vcm-7304.vm.duke.edu:5000``. All GET and POST requests for project can be send this address.