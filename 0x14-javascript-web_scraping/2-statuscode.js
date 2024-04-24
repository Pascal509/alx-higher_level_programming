#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Perform a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  // Print the status code of the response
  console.log(`code: ${response.statusCode}`);
});
