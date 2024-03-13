#!/usr/bin/bash
const Square = require('./5-square');

class mySquare extends Square{
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width))
    }
  }  
}
module.exports = mySquare;
