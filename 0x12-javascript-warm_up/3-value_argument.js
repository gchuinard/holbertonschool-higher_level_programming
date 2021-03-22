#!/usr/bin/node
let count = 0;
process.argv.forEach((value, index) => {
  count++;
  if (count > 2) {
    console.log(`${value}`);
  }
});
if (count === 2) {
  console.log('No argument');
}
