#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      return;
    }
    for (let i = 0; i < this.height; i++) {
      let repeatString = '';
      for (let j = 0; j < this.width; j++) {
        repeatString += 'X';
      }
      console.log(repeatString);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
