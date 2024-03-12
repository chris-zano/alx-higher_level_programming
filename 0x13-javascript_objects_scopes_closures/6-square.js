#!/usr/bin/node
// square inherits from rectangle

const Squarep = require('./5-square');

module.exports = class Square extends Squarep {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
