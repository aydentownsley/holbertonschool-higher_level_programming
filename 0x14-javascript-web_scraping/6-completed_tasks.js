#!/usr/bin/node
const request = require('request');
const url = process.argv[2].toString();
let k = 0;
const newDict = {};
let key = -1;
let data;

request(url, function (err, res, body) {
  if (err) {
    return console.log(err);
  } else {
    data = JSON.parse(body);
    for (const i in data) {
      if (key !== data[i].userId) { k = 0; }
      key = data[i].userId;
      if (data[i].completed === true) {
        newDict[key] = k += 1;
      }
    }
    for (const s in newDict) {
      if (newDict[s] === 0) { delete newDict[s]; }
    }
    console.log(newDict);
  }
});
