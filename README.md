# Heart Rate Sentinel Server

A simple centralized heart rate sentinel server. This server will be built to receive POST requests from mock patient heart rate monitors that contain patient heart rate information over time. If a patient exhibits a tachycardic heart rate, the physician should receive an email warning them. This calculation should be based on age and heart rate.

#### Travis contiuous integration status
[![Build Status](https://travis-ci.com/mdholbrook/heart_rate_sentinel_server.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)