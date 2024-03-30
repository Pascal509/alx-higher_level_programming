#!/bin/bash
# Send a POST request with a specific data to trigger the server response
curl -s -X POST -d "user_id=98" 0.0.0.0:5000/catch_me
