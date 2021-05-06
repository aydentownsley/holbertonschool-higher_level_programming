#!/usr/bin/node
const request = require('request');
const url_string = process.argv.slice(2);

request.get(String(url_string), (err, res) => {
  if (err) {
    return console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
