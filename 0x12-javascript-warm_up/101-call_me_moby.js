#!/usr/bin/node
exports.callMeMoby = function (x, fct) {
  while (x > 0) {
    fct();
    x--;
  }
};
