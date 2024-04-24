#!/bin/bash
# Bash script that takes in a URL, sends a GET request, and displays the body of the response
curl -s -o response.txt -w "%{http_code}" "$1" | { read -r status_code && [ "$status_code" -eq 200 ] && cat response.txt || echo "Non-200 status code: $status_code";}
