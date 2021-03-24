#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        line = line.concat('X');
      }
      console.log(line);
      line = '';
    }
  }
};
