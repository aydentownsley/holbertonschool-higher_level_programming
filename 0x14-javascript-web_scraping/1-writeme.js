#!/usr/bin/node
const file = process.argv.slice(2);
const content = process.argv.slice(3);

const fs = require('fs');
fs.writeFile(String(file[0]), String(content), err => {
  if (err) {
    return console.log(err);
  }
  // file gets written
});
