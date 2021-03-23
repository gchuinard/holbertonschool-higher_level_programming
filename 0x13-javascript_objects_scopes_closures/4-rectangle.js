#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    let height;
    let width;
    let rect;

    height = this.height;
    while (height > 0) {
      width = this.width;
      rect = '';
      while (width > 0) {
        rect += c;
        width--;
      }
      console.log(rect);
      height--;
    }
  }

  rotate () {
    const tmp = this.width;

    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
