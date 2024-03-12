#!/usr/bin/node
const process = require('process');
if (Number(process.argv[2])) {
  const myNumber = Number(process.argv[2]);
  console.log('My number: ' + myNumber);
} else {
  console.log('Not a number');
}
