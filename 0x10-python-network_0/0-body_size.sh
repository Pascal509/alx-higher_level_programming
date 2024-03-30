#!/bin/bash
# Bash script takes in a URL and displays the size of the body of the response
curl -sI 'https://reqbin.com/echo' | grep -i Content-Length
