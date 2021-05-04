#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.

const process = require('process');
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const file = args[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(file, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
