#!/usr/bin/node
const request = require('request');
const url = process.argv[2].toString();
let k = 1;
const newDict = {};
let key = 1;
let data;

request(url, function (err, res) {
  if (err) {
    return console.log(err);
  } else {
    data = JSON.parse(res.body);
    for (const i in data) {
      if (data[i].completed === true) {
        if (key !== data[i].userId) { k = 1; }
        key = data[i].userId;
        newDict[key] = k++;
      }
    }
    for (const s in newDict) {
      if (newDict[s] === 0) { delete newDict[s]; }
    }
    console.log(newDict);
  }
});
