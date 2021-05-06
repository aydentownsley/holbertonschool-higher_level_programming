#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2].toString();
const file = process.argv[3].toString();

request(url, function (err, res) {
  if (err) {
    return console.log(err);
  } else {
    fs.writeFile(file, res.body, 'utf8', err => {
      if (err) {
        return console.log(err);
      }
      // file gets written
    });
  }
});
