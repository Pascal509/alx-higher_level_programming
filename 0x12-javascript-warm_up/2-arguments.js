#!/usr/bin/node
/* Write a script that prints a message depending of
 * the number of arguments passed
 */
const myProcess = process.argv.length - 2;

if (myProcess === 0) {
  console.log('No argument');
}  else if (myProcess === 1) {
  console.log('Argument found');
}  else {
  console.log('Arguments found');
}
