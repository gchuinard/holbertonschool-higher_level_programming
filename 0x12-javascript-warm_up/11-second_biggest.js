#!/usr/bin/node

let sec = 0;
let pri = 0;

process.argv.forEach((value) => {
  parseInt(value);
  if (value > pri) {
    sec = pri;
    pri = value;
  } else if (value < pri && pri === sec) {
    sec = value;
  }
});

console.log(sec);
