#!/bin/bash
url='https://reqbin.com/echo'
curl -sI $url | grep -i Content-Length
