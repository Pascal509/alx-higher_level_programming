#!/usr/bin/node
// import modules
const request = require('request');
const fs = require('fs');

// The command line arguments is the URL
const url = process.argv[2];
const filePath = process.argv[3];

// Function to fetch the content and write it to the file
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Write the fetched content to the file specified by the user
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Failed to write to file:', err);
    }
  });
});
