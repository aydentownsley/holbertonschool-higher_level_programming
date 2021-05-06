#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2).toString();
let k = 0;

request(url, function (err, body) {
  if (err) {
    return console.log(err);
  } else {
    const resArray = JSON.parse(body.body).results;
    for (const i in resArray) {
      for (const x in resArray[i].characters) {
        if (resArray[i].characters[x].includes('18')) {
          k++;
        }
      }
    }
    console.log(k);
  }
});
