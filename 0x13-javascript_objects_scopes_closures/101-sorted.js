#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
let i;

for (const key in dict) {
  if (newDict[dict[key]]) {
    i = newDict[dict[key]].length;
    if (newDict[dict[key]]) {
      newDict[dict[key]][i] = key;
    }
  } else {
    i = 0;
    newDict[dict[key]] = [];
    newDict[dict[key]][i] = key;
  }
}
console.log(newDict);
