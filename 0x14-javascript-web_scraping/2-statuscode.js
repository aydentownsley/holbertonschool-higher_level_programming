#!/usr/bin/node
const request = require('request');
const urlString = process.argv.slice(2);

request.get(String(urlString), (err, res) => {
  if (err) {
    return console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
