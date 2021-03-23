#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let height;
    let width;
    let sqr;

    height = this.size;
    while (height > 0) {
      width = this.size;
      sqr = '';
      while (width > 0) {
        sqr += c;
        width--;
      }
      console.log(sqr);
      height--;
    }
  }
}
module.exports = Square;
