#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const chr = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
