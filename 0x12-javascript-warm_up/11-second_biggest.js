#!/usr/bin/node

let sec = 0;
let pri = 0;

process.argv.forEach((value, index) => {
  value = parseInt(value);
  pri = parseInt(pri);
  if (pri < value) {
    sec = pri;
    pri = value;
  } else if (sec < value) {
    sec = value;
  } else if (index === 2 && value < 0) {
    pri = value;
  }
});

console.log(sec);
