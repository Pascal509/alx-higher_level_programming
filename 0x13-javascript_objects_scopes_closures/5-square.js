#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class mySquare extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = mySquare;
