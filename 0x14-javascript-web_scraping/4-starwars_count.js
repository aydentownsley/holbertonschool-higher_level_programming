#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2);
const character = 'https://swapi-api.hbtn.io/api/people/18/';
let i; let k = 0;

request.get(url.toString(), function (err, body) {
  if (err) {
    return console.log(err);
  } else {
    const dict = JSON.parse(body.body);
    for (i = 0; i < 7; i++) {
      if (dict.results[i].characters.includes(character)) {
        k++;
      }
    }
    console.log(k);
  }
});
