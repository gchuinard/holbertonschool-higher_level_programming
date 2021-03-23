#!/usr/bin/node
const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c = 'X') {
    super.print(c);
  }
}
module.exports = Square;
