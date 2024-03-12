#!/usr/bin/node
// count number of logs

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
