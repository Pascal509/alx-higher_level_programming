#!/bin/bash
# Bash script takes in a URL and displays the size of the body of the response
curl -sI 'http://0.0.0.0:5000' | grep -i Content-Length | awk '{print $2}'
