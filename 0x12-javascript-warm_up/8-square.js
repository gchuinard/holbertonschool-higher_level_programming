#!/usr/bin/node
const size = parseInt(process.argv[2]);
let height;
let length;
let square;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  length = size;
  while (length > 0) {
    height = size;
    square = '';
    while (height > 0) {
      square += '#';
      height--;
    }
    console.log(square);
    length--;
  }
}
