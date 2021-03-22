#!/usr/bin/node
let count = 0;
process.argv.forEach((value, index) => {
  count++;
});
if (count === 3) {
  console.log('Argument found');
} else if (count > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
