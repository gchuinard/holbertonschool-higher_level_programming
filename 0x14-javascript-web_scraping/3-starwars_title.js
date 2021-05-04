#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.

const process = require('process');
const request = require('request');
const args = process.argv;
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = args[2];
const url = apiUrl + movieId;
const options = { json: true };

request(url, options, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(body.title);
});
