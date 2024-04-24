#!/usr/bin/node

// Import the fs module to interact with the file system
const fs = require('node:fs');

const filePath = process.argv[2];

fs.readFile = (filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
