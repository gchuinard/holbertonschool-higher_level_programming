#!/usr/bin/node
// Display the status code of a GET request.

const process = require('process');
const request = require('request');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
