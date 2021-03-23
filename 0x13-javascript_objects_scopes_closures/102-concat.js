#!/usr/bin/node

const file = require('fs');
const fileA = process.argv[2];
const textA = file.readFile(fileA, 'utf8');
const fileB = process.argv[3];
const textB = file.readFile(fileB, 'utf8');
const fileC = process.argv[4];
file.writeFile(fileC, textA + textB);
