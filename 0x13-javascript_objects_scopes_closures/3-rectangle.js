#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let height;
    let width;
    let rect;

    height = this.height;
    while (height > 0) {
      width = this.width;
      rect = '';
      while (width > 0) {
        rect += 'X';
        width--;
      }
      console.log(rect);
      height--;
    }
  }
}
module.exports = Rectangle;
