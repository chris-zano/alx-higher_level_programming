#!/usr/bin/node
// sort

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map((key) => {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  return newDict[dict[key]].push(key);
});

console.log(newDict);
