#!/usr/bin/node
const request = require('request');
const movieId = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request.get(url, function (err, res, body) {
  if (err) {
    return console.log(err);
  } else {
    return console.log(JSON.parse(body).title);
  }
});
