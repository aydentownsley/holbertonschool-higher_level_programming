#!/usr/bin/node

const superSquare = require('./5-square');

module.exports = class Square extends superSquare {
  charPrint (c = 'X') {
    let line = '';
    for (let x = 0; x < this.width; x++) {
      for (let y = 0; y < this.width; y++) {
        line = line.concat(c);
      }
      console.log(line);
      line = '';
    }
  }
};
