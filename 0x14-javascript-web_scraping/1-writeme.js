#!/usr/bin/node

// Import the fs module to handle file operations
const fs = require('fs');

// Get command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
