#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2].toString();
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let charUrlList;
let char;

request(url, function (err, res, body) {
  if (err) {
    return console.log(err);
  } else {
    charUrlList = JSON.parse(body).characters;
    for (const i in charUrlList) {
      request.get(charUrlList[i], function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          char = JSON.parse(body).name;
          console.log(char);
        }
      });
    }
  }
});
