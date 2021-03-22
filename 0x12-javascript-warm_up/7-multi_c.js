#!/usr/bin/node
let nbr = parseInt(process.argv[2]);
if (isNaN(nbr)) {
  console.log('Missing number of occurrences');
} else {
  while (nbr > 0) {
    console.log('C is fun');
    nbr--;
  }
}
