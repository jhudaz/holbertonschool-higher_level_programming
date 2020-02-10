#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    const chr = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}

module.exports = Square;
